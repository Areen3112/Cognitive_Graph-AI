# controller_llm.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure the API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

genai.configure(api_key=api_key)

# Use Gemini 1.5 Flash
model = genai.GenerativeModel("models/gemini-1.5-flash")


def get_next_thought(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"[ERROR] Gemini failed: {e}")
        return "Error generating response. Please try again later."
