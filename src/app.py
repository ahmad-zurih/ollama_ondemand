import os
import streamlit as st

# ------------------------------------------------------------------------------
# IMPORTANT NOTE:
# This is a simple example to demonstrate how to secure a Streamlit app with
# a token against brute force session attacks for use with Open OnDemand.
#
# This is a simple method to ensure that only those with the correct token can
# access the OnDemand app. This is not a secure way to authenticate users.
# Please use a more secure method for apps accessible from the internet.
# ------------------------------------------------------------------------------

TOKEN = os.environ.get("TOKEN")
if TOKEN is None:
    raise ValueError("TOKEN is not set. Please set the TOKEN in your environment variables.")

query_params = st.query_params
user_token = query_params.get("token")

# Authentication Check
if user_token == TOKEN:
    authenticated = True
    st.success("Authentication Successful!")
else:
    authenticated = False
    st.error("Access Denied: Invalid or Missing Token")
    st.stop()  # Stop execution if authentication fails

# Display user information after authentication
if authenticated:
    st.title("Streamlit OnDemand App")
    st.write("""
    Hello *world*!
    """)
