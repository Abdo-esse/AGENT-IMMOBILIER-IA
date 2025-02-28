import streamlit as st
from services.property_agent import PropertyFindingAgent
from utils.config import setup_api_keys
from datetime import datetime

def create_property_agent():
    """Create PropertyFindingAgent with API keys from session state"""
    if 'property_agent' not in st.session_state:
        st.session_state.property_agent = PropertyFindingAgent(
            firecrawl_api_key=st.session_state.firecrawl_key,
            openai_api_key=st.session_state.openai_key,
            model_id=st.session_state.model_id
        )

def main():
    # Configuration de la page avec thème moderne
    st.set_page_config(
        page_title="PropertyGPT | Votre Agent Immobilier IA",
        page_icon="🏡",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # CSS personnalisé pour une interface plus moderne
    st.markdown("""
    <style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        height: 3rem;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    div.stTabs {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 10px;
    }
    div[data-testid="stExpander"] {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }
    </style>
    """, unsafe_allow_html=True)

    setup_api_keys()

    # Barre latérale améliorée
    with st.sidebar:
        st.image("https://via.placeholder.com/150x70", caption="PropertyGPT")
        st.title("⚙️ Configuration")
        
        # Organisation en onglets pour la configuration
        sidebar_tabs = st.tabs(["🔑 API Keys", "⚡ Performance", "ℹ️ À propos"])
        
        with sidebar_tabs[0]:
            st.session_state.firecrawl_key = st.text_input(
                "Clé API Firecrawl",
                type="password",
                help="Entrez votre clé API Firecrawl"
            )
            st.session_state.openai_key = st.text_input(
                "Clé API OpenAI",
                type="password",
                help="Entrez votre clé API OpenAI"
            )
        
        with sidebar_tabs[1]:
            st.session_state.model_id = st.selectbox(
                "Modèle IA",
                options=["o3-mini", "gpt-4o", "claude-3-sonnet", "gemini-pro"],
                help="Sélectionnez le modèle IA à utiliser"
            )
            st.session_state.search_depth = st.slider(
                "Profondeur de recherche",
                min_value=1,
                max_value=5,
                value=3,
                help="Définit la profondeur de recherche (plus élevé = plus de résultats, mais plus lent)"
            )
        
        with sidebar_tabs[2]:
            st.info("PropertyGPT v1.2.0")
            st.markdown("Développé par votre équipe")
            st.markdown("[Documentation](https://example.com)")
            
        # Validation des clés API
        if st.session_state.firecrawl_key and st.session_state.openai_key:
            create_property_agent()
            st.success("✅ Configuration validée!")
        else:
            st.warning("⚠️ Veuillez configurer vos clés API")

    # Section principale avec logo et titre
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("https://via.placeholder.com/100", width=80)
    with col2:
        st.title("PropertyGPT | Votre Agent Immobilier IA")
        st.markdown("*Trouvez la propriété idéale avec l'aide de l'intelligence artificielle*")

    # Interface principale organisée en onglets
    tabs = st.tabs(["🔍 Recherche", "📊 Analyses", "💼 Mes recherches"])
    
    with tabs[0]:
        # Formulaire de recherche amélioré
        with st.form(key="search_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                city = st.text_input("Ville", placeholder="Ex: Bangalore, Mumbai, Delhi")
                property_category = st.selectbox(
                    "Catégorie", 
                    options=["Résidentiel", "Commercial", "Terrain", "Industriel"]
                )
                
            with col2:
                max_price = st.number_input(
                    "Budget maximum (en Crores)", 
                    min_value=0.1, 
                    max_value=100.0, 
                    value=5.0, 
                    step=0.1,
                    format="%.1f"
                )
                property_type = st.selectbox(
                    "Type de propriété", 
                    options=[
                        "Appartement", 
                        "Maison individuelle", 
                        "Villa",
                        "Penthouse",
                        "Studio"
                    ]
                )
            
            # Options avancées dans un expander
            with st.expander("Options avancées"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    min_area = st.number_input("Surface minimum (m²)", min_value=10, value=50)
                with col2:
                    bedrooms = st.number_input("Chambres", min_value=1, max_value=10, value=2)
                with col3:
                    sort_by = st.selectbox(
                        "Trier par", 
                        options=["Prix (croissant)", "Prix (décroissant)", "Surface", "Date de publication"]
                    )
            
            submit_search = st.form_submit_button(
                label="🔍 Lancer la recherche", 
                use_container_width=True
            )
        
        # Traitement de la recherche
        if submit_search:
            if 'property_agent' not in st.session_state:
                st.error("⚠️ Veuillez configurer vos clés API dans la barre latérale!")
                return
                
            if not city:
                st.error("⚠️ Veuillez entrer une ville!")
                return
                
            try:
                # Enregistrement de la recherche dans l'historique
                if 'search_history' not in st.session_state:
                    st.session_state.search_history = []
                    
                st.session_state.search_history.append({
                    "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "city": city,
                    "type": property_type,
                    "price": max_price
                })
                
                with st.status("Recherche en cours...") as status:
                    st.write("🔍 Recherche de propriétés...")
                    property_results = st.session_state.property_agent.find_properties(
                        city=city,
                        max_price=max_price,
                        property_category=property_category,
                        property_type=property_type
                    )
                    
                    st.write("📊 Analyse des tendances du marché...")
                    location_trends = st.session_state.property_agent.get_location_trends(city)
                    
                    status.update(label="✅ Recherche terminée!", state="complete")
                
                # Affichage des résultats de propriétés
                st.subheader("🏘️ Propriétés recommandées")
                
                # Division des résultats en cartes
                property_cards = st.columns(2)
                
                # Simulation de résultats de propriétés pour l'exemple
                # Normalement, vous analyseriez et diviseriez les résultats réels retournés par l'API
                with property_cards[0]:
                    with st.container():
                        st.image("https://via.placeholder.com/400x200", use_column_width=True)
                        st.markdown(f"**Appartement Premium à {city}**")
                        st.markdown("3 BHK | 1500 sq.ft | 3.2 Cr")
                        st.progress(85, text="Score de correspondance: 85%")
                        with st.expander("Détails"):
                            st.markdown(property_results[:500] + "...")
                
                with property_cards[1]:
                    with st.container():
                        st.image("https://via.placeholder.com/400x200", use_column_width=True)
                        st.markdown(f"**Villa de luxe à {city}**")
                        st.markdown("4 BHK | 2200 sq.ft | 4.5 Cr")
                        st.progress(78, text="Score de correspondance: 78%")
                        with st.expander("Détails"):
                            st.markdown(property_results[500:1000] + "...")
                
                # Analyse complète dans un expander
                with st.expander("📑 Rapport d'analyse complet"):
                    st.markdown(property_results)
                    
                # Tendances du marché
                st.subheader("📈 Analyse des tendances du marché")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric(
                        label="Prix moyen au m²", 
                        value="₹12,500", 
                        delta="3.2%",
                        delta_color="inverse"
                    )
                    st.write("La tendance des prix au m² dans cette zone est en hausse.")
                    
                with col2:
                    st.metric(
                        label="Offre disponible", 
                        value="453 propriétés", 
                        delta="-5%"
                    )
                    st.write("Le nombre de propriétés disponibles est en baisse.")
                
                with st.expander("📊 Analyse détaillée de l'emplacement"):
                    st.markdown(location_trends)
                    
            except Exception as e:
                st.error(f"❌ Une erreur s'est produite: {str(e)}")
    
    with tabs[1]:
        st.subheader("📊 Analyses du marché immobilier")
        
        analysis_type = st.selectbox(
            "Type d'analyse",
            options=["Tendances des prix", "Retour sur investissement", "Prévisions du marché"]
        )
        
        st.info("Sélectionnez une ville et lancez une analyse pour voir les tendances du marché immobilier.")
        
        city_for_analysis = st.text_input("Ville à analyser", placeholder="Ex: Bangalore")
        
        if st.button("Générer l'analyse", use_container_width=True):
            st.write("Fonctionnalité en développement")
    
    with tabs[2]:
        st.subheader("💼 Historique de vos recherches")
        
        if 'search_history' not in st.session_state or not st.session_state.search_history:
            st.info("Aucune recherche enregistrée. Lancez une recherche pour voir l'historique.")
        else:
            for i, search in enumerate(reversed(st.session_state.search_history)):
                with st.container():
                    col1, col2, col3 = st.columns([1, 3, 1])
                    with col1:
                        st.write(search["date"])
                    with col2:
                        st.write(f"**{search['city']}** - {search['type']} - {search['price']} Cr")
                    with col3:
                        if st.button("Relancer", key=f"reload_{i}"):
                            st.rerun()
                st.divider()

    # Pied de page
    st.divider()
    st.markdown("""
    <div style="text-align: center; opacity: 0.7;">
        © 2025 PropertyGPT | Propulsé par l'IA | Données immobilières en temps réel
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()