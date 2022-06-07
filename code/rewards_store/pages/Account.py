from pathlib import Path
from web3 import Web3, Account
from dotenv import load_dotenv
from sqlite3 import Date

import pandas as pd
import requests
import os
import streamlit as st
import json
import numpy as np

# Declare local Ganache HTTP provider
local_ganache_http_provider = 'HTTP://127.0.0.1:7545'

# Connect to the local Ganache HTTP provider
w3=Web3(Web3.HTTPProvider(local_ganache_http_provider))

load_dotenv()
contract_address = os.getenv('CONTRACT_ADDRESS')
contract_owner_address = os.getenv('CONTRACT_OWNER_ADDRESS')
contract_owner_pvt_key = os.getenv('CONTRACT_OWNER_PVT_KEY')

# Load Application Binary Interface (abi) file as JSON

with open('contract_abi.txt') as contract_abi_file:
    contract_abi_json = json.load(contract_abi_file)

# Connect to the deployed contract
rt_contract = w3.eth.contract(contract_address, abi=contract_abi_json)

# Get all accounts from local Ganache provider
accounts = w3.eth.accounts

# Remove contract owner address from accounts as we
# DO NOT want to use the owner address for transacations.
accounts.remove(contract_owner_address)

# Set Webpage Name
st.set_page_config(page_title="Account Info", layout="centered")

# Account Balance
st.header("🛍️")
st.header("Rewards Store")

# Select Account
selected_account = st.selectbox(
    "Choose an account:",
    accounts,0)

'Balance:', f"{(rt_contract.functions.balanceOf(selected_account).call())/(10**18)} RT Tokens"


reward_options_df = pd.read_csv("rewards_options.csv")

# Set Webpage Name
# st.set_page_config(page_title="Rewards Store", layout="centered")

st.markdown("---")

# Select Reward
selected_reward = st.selectbox(
    "Choose a reward:",
    reward_options_df.Item,0)
# st.write(f"You selected {selected_reward}")

# Display Selected Reward Price
selected_reward_price = reward_options_df.loc[reward_options_df.Item == selected_reward]["Price (Coins)"].iloc[0]
selected_reward_price=np.asscalar(selected_reward_price)
st.write(f"The {selected_reward} is available for {selected_reward_price} coins.")

# Display Selected Reward Image
selected_reward_image = reward_options_df.loc[reward_options_df.Item == selected_reward]["URL"].iloc[0]
st.image(selected_reward_image)

item_count = st.number_input(
    "How many would you like?",min_value=1)
# amount_spent = int(amount_spent)

def buy_selected_item(**kwargs):
    """
    For a given account:
    account_balance >= selected_item_price * item_count
    if yes:
        Buy successful
    else:
        Fail, insufficient balance
    """
    account_no = kwargs['account_no']
    selected_item_price = kwargs['selected_item_price']
    item_count = kwargs['item_count']
    
    # st.text_area("",value=f"Account {account_no} would like to buy items worth {item_count * selected_item_price} RT Tokens.")
    
    total_price = item_count * selected_item_price * (10**18)
    account_balance = rt_contract.functions.balanceOf(account_no).call()
    if total_price > account_balance:
        st.error(f"Insufficient Balance. You need {(total_price - account_balance)/(10**18)} additional RT tokens.")
    else:
        
        txn = {
        'from': contract_owner_address,
        'nonce': w3.eth.get_transaction_count(contract_owner_address),
        'gasPrice': w3.eth.gas_price
        }
        
        # st.write(rt_contract.functions.allowance(account_no, contract_owner_address).call())
        tx_hash = rt_contract.functions.approve(contract_owner_address, total_price).transact({'from': account_no})
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        # st.write(rt_contract.functions.allowance(account_no, contract_owner_address).call())
    
        raw_txn = rt_contract.functions.transferFrom(account_no, contract_owner_address, total_price).buildTransaction(txn)
        signed_txn = w3.eth.account.signTransaction(raw_txn, private_key=contract_owner_pvt_key)
        txn_response = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        st.success(f"Purchase Successful. New Balance for {account_no}: {rt_contract.functions.balanceOf(account_no).call()/(10**18)}")

buy_kwargs= {}
buy_kwargs['account_no'] = selected_account
buy_kwargs['selected_item_price'] = selected_reward_price
buy_kwargs['item_count'] = item_count

if st.button("Buy"): 
    buy_selected_item(**buy_kwargs)