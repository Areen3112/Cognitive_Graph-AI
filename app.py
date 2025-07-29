# app.py

import streamlit as st
from controller_llm import get_next_thought

st.title("Cognitive Graph AI 🌐")

user_input = st.text_input("What's your idea or topic?")

if st.button("Generate Thought"):
    if user_input:
        response = get_next_thought(user_input)
        st.success(response)
    else:
        st.warning("Please enter a topic first.")
