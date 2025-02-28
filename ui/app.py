import streamlit as st
from services.property_agent import PropertyFindingAgent
from utils.config import setup_api_keys

def create_property_agent():
    """Create PropertyFindingAgent with API keys from session state"""
    if 'property_agent' not in st.session_state:
        st.session_state.property_agent = PropertyFindingAgent(
            firecrawl_api_key=st.session_state.firecrawl_key,
            openai_api_key=st.session_state.openai_key,
            model_id=st.session_state.model_id
        )

def main():
    st.set_page_config(
        page_title="AI Real Estate Agent",
        page_icon="🏠",
        layout="wide"
    )

    setup_api_keys()

    with st.sidebar:
        st.title("🔑 API Configuration")
        st.session_state.model_id = st.selectbox(
            "Choose OpenAI Model",
            options=["o3-mini", "gpt-4o"],
            help="Select the AI model to use."
        )
        st.session_state.firecrawl_key = st.text_input(
            "Firecrawl API Key",
            type="password",
            help="Enter your Firecrawl API key"
        )
        st.session_state.openai_key = st.text_input(
            "OpenAI API Key",
            type="password",
            help="Enter your OpenAI API key"
        )
        
        if st.session_state.firecrawl_key and st.session_state.openai_key:
            create_property_agent()

    st.title("🏠 AI Real Estate Agent")
    st.info("Welcome to the AI Real Estate Agent!")

    city = st.text_input("City", placeholder="Enter city name (e.g., Bangalore)")
    property_category = st.selectbox("Property Category", options=["Residential", "Commercial"])
    max_price = st.number_input("Maximum Price (in Crores)", min_value=0.1, max_value=100.0, value=5.0, step=0.1)
    property_type = st.selectbox("Property Type", options=["Flat", "Individual House"])

    if st.button("🔍 Start Search", use_container_width=True):
        if 'property_agent' not in st.session_state:
            st.error("⚠️ Please enter your API keys in the sidebar first!")
            return
            
        if not city:
            st.error("⚠️ Please enter a city name!")
            return
            
        try:
            with st.spinner("🔍 Searching for properties..."):
                property_results = st.session_state.property_agent.find_properties(
                    city=city,
                    max_price=max_price,
                    property_category=property_category,
                    property_type=property_type
                )
                st.success("✅ Property search completed!")
                st.subheader("🏘️ Property Recommendations")
                st.markdown(property_results)
                
                with st.spinner("📊 Analyzing location trends..."):
                    location_trends = st.session_state.property_agent.get_location_trends(city)
                    st.success("✅ Location analysis completed!")
                    with st.expander("📈 Location Trends Analysis of the city"):
                        st.markdown(location_trends)
                
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")