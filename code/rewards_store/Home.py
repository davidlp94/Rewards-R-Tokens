import streamlit as st

# Set Webpage Name
st.set_page_config(page_title="Rewards ‘R Tokens", layout="centered")
st.header("Rewards 'R Tokens")
st.subheader("Earn Rewards by Using Your Credit Card!")

def home():
    st.markdown("# Home 🎈")
    st.sidebar.markdown("# Home 🎈")
    
def account():
    st.markdown("# Account Balance 🏦")
    st.sidebar.markdown("# Account Balance 🏦")
    
def store():
    st.markdown("# Rewards Store 🛍️")
    st.sidebar.markdown("# Rewards Store 🛍️")
    
page_names_to_funcs = {
    "Home": home,
    "My Account": account,
    "Rewards Store": store,
}

#selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()

st. write("Welcome to the future of credit card rewards! We're happy to have you. Rewards 'R Tokens will award you special RT tokens for all your credit card purchases. These tokens can be redeemed in the RT Rewards Store for electronics, home goods, food/drinks, and much more. Simply spend with your credit card and treat yourself!")