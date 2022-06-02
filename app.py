import os
from sqlite3 import Date
import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv
from pathlib import Path

reward_options_df = pd.read_csv("rewards_options.csv")

# Set Webpage Name
st.set_page_config(page_title="Rewards ‘R Tokens", layout="centered")
st.header("Rewards 'R Tokens")
st.subheader("Earn Rewards by Using Your Credit Card!")

# Rewards Balance
st.sidebar.header("Your Rewards Balance:")
st.sidebar.write("123XYZ Coins")

st.sidebar.markdown("---")

st.sidebar.header("Record a Credit Card Purchase")

# Get Amount Spent
amount_spent = st.sidebar.number_input(
    "How much money did you spend?",min_value=1)
amount_spent = int(amount_spent)

# Get Category
category = st.sidebar.selectbox(
    "What did you purchase?",
    ("Gas","Food & Dining","Travel","Other"))

# Submit Transaction
st.sidebar.button("Submit transaction")

# Select Reward
selected_reward = st.selectbox(
    "Choose a reward:",
    reward_options_df.Item,0)
# st.write(f"You selected {selected_reward}")

# Display Selected Reward Price
selected_reward_price = reward_options_df.loc[reward_options_df.Item == selected_reward]["Price (Coins)"].iloc[0]
st.write(f"The {selected_reward} is available for {selected_reward_price} coins.")

# Display Selected Reward Image
selected_reward_image = reward_options_df.loc[reward_options_df.Item == selected_reward]["URL"].iloc[0]
st.image(selected_reward_image)