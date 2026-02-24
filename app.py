import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="Simple Chatbot")

st.title("🤖 Simple ChatGPT Clone")

# Sidebar
with st.sidebar:
    st.header("Sidebar")
    st.write("This is a simple offline chatbot.")

# Simple bot reply function
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi there! 👋 How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! 😄"
    elif "chhattisgarh" in user_input:
        return "Chhattisgarh is known as the Rice Bowl of India 🌾"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day 😊"
    else:
        responses = [
            "Tell me more!",
            "That's interesting 🤔",
            "Can you explain more?",
            "I see!",
        ]
        return random.choice(responses)

# Store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot reply
    bot_reply = chatbot_response(user_input)

    # Save bot reply
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display bot reply
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
