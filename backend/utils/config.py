import os

def get_openai_api_key():
    """
    Load OpenAI API key in a cloud-safe way.
    Priority:
    1. Streamlit secrets (Streamlit Cloud)
    2. Environment variables (local / Docker)
    """
    try:
        import streamlit as st
        if "OPENAI_API_KEY" in st.secrets:
            return st.secrets["OPENAI_API_KEY"]
    except Exception:
        pass

    key = os.getenv("OPENAI_API_KEY")
    if key:
        return key

    raise RuntimeError("OPENAI_API_KEY not found in environment or Streamlit secrets")


OPENAI_API_KEY = get_openai_api_key()

