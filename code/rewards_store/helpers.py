import streamlit as st

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
    
    st.write(f"Account {account_no} would like to buy items worth {item_count * selected_item_price} ")