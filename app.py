import streamlit as st
from google.genai import Client
import os

# Set page config
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
with st.sidebar:
    st.title("hello")

    
# Title
st.title("🤖 Gemini AI Chatbot")



# User input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

  

  
