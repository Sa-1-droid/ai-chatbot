import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("Niggabot(Saawan) is at you rescue")


if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    st.chat_message("user").markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Send conversation to model
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    # Show bot reply
    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })