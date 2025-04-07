import os
import streamlit as st
import requests
import json

# ------------------------------------------------------------------------------
# IMPORTANT NOTE:
# This Streamlit app is secured with a token against brute force session attacks 
# for use with Open OnDemand.
#
# This is a simple method to ensure that only those with the correct token can
# access the OnDemand app. This is not a secure way to authenticate users.
# Please use a more secure method for apps accessible from the internet.
# ------------------------------------------------------------------------------

# Function to send a request to Ollama
def ollama_chat(full_prompt):
    ollama_host = os.environ['OLLAMA_HOST']
    url = f"http://{ollama_host}/api/generate"
    payload = {"prompt": full_prompt}
    response = requests.post(url, json=payload, timeout=300)
    if response.status_code == 200:
        data = response.json()
        # Handle old/new JSON format
        if isinstance(data, list):
            # each item might have "content"
            result = "".join([chunk["content"] for chunk in data if "content" in chunk])
        elif isinstance(data, dict):
            result = data.get("content", "")
        else:
            result = "Error parsing response."
        return result
    else:
        return f"Error {response.status_code}: {response.text}"
    

def process_conversation():
    # Initialize session state for chat
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    user_input = st.text_input("Your prompt:", key="prompt_input")

    # On button click, send prompt to Ollama
    if st.button("Send"):
        st.session_state["messages"].append({"role": "user", "content": user_input})
        conversation = ""
        for msg in st.session_state["messages"]:
            role = msg["role"]
            text = msg["content"]
            conversation += f"{'User' if role=='user' else 'Assistant'}: {text}\n"

        answer = ollama_chat(conversation)
        st.session_state["messages"].append({"role": "assistant", "content": answer})

    # Display the conversation
    for msg in st.session_state["messages"]:
        role = msg["role"]
        text = msg["content"]
        if role == "user":
            st.markdown(f"**User:** {text}")
        else:
            st.markdown(f"**Assistant:** {text}")


TOKEN = os.environ.get("TOKEN")
if TOKEN is None:
    raise ValueError("TOKEN is not set. Please set the TOKEN in your environment variables.")

query_params = st.query_params
user_token = query_params.get("token")

# Authentication Check
if user_token == TOKEN:
    st.set_page_config(page_title="Ollama Chat", layout="wide")
    st.title("DSL Ollama Chat")
    process_conversation()
else:
    st.error("Access Denied: Invalid or Missing Token")
    st.stop()  # Stop execution if authentication fails