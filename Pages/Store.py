import os
from sqlite3 import Date
import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv
from pathlib import Path

reward_options_df = pd.read_csv("rewards_options.csv")

# Set Webpage Name
st.set_page_config(page_title="Rewards Store", layout="centered")

# Rewards Balance
st.header("🛍️")
st.header("Rewards Store")

st.markdown("---")

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