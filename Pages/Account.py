import streamlit as st

# Set Webpage Name
st.set_page_config(page_title="Account Info", layout="centered")

# Rewards Balance
st.header("🏦")
st.header("Your Rewards Balance")
st.write("123XYZ Coins")

st.markdown("---")

st.subheader("Record a Credit Card Purchase")

# Get Amount Spent
amount_spent = st.number_input(
    "How much money did you spend?",min_value=1)
amount_spent = int(amount_spent)

# Get Category
category = st.selectbox(
    "What did you purchase?",
    ("Gas","Food & Dining","Travel","Other"))

# Submit Transaction
st.button("Submit transaction")