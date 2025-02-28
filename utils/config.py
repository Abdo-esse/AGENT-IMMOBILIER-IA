import streamlit as st

def setup_api_keys():
    """Configure API keys from Streamlit session state"""
    if 'firecrawl_key' not in st.session_state:
        st.session_state.firecrawl_key = None
    if 'openai_key' not in st.session_state:
        st.session_state.openai_key = None
    if 'model_id' not in st.session_state:
        st.session_state.model_id = "o3-mini"