# AI Real Estate Agent

## Introduction
L'**AI Real Estate Agent** est une application web qui utilise l'intelligence artificielle pour aider les utilisateurs à trouver et analyser des propriétés immobilières en fonction de leurs préférences. L'application est construite avec **Streamlit** pour l'interface utilisateur et utilise des API externes comme **Firecrawl** et **OpenAI** pour extraire et analyser les données.

---

## Fonctionnalités
- **Recherche de propriétés** :
  - Trouver des propriétés en fonction de la ville, du type de propriété et du budget.
  - Analyser les propriétés et fournir des recommandations détaillées.
  
- **Analyse des tendances du marché** :
  - Obtenir des informations sur les tendances des prix par localité.
  - Identifier les meilleures zones d'investissement.

- **Interface utilisateur moderne** :
  - Interface intuitive et réactive.
  - Design personnalisé avec CSS.

---

## Structure du Projet

Voici la structure des fichiers du projet :
├── main.py # Point d'entrée de l'application
├── models/ # Dossier pour les modèles Pydantic
│ └── schemas.py # Schémas de données pour la validation
├── services/ # Dossier pour les services métier
│ └── property_agent.py # Logique de l'agent de recherche de propriétés
├── utils/ # Dossier pour les utilitaires
│ └── config.py # Gestion de la configuration (clés API, etc.)
├── ui/ # Dossier pour l'interface utilisateur
│ ├── init.py # Fichier vide pour indiquer que ui est un package
│ └── app.py # Logique de l'interface utilisateur avec Streamlit
└── requirements.txt # Fichier des dépendances

## Dépendances
Les dépendances du projet sont listées dans le fichier `requirements.txt`. Pour installer les dépendances, exécutez :

```bash
pip install -r requirements.txt

## Dépendances principales
- **streamlit** : Framework pour créer des applications web interactives.
- **pydantic** : Bibliothèque pour la validation des données.
- **firecrawl** : API pour extraire des données web.
- **agno** : Bibliothèque pour interagir avec des modèles d'IA.

---

## Comment exécuter le projet
1. Clonez le dépôt du projet.
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt


## Utilisation de l'application

### Configuration des API
- Dans la barre latérale, entrez vos clés API pour **Firecrawl** et **OpenAI**.
- Sélectionnez le modèle AI à utiliser.

### Recherche de propriétés
- Entrez la ville, le type de propriété et votre budget maximum.
- Cliquez sur **🔍 Lancer la recherche** pour obtenir des recommandations.

### Analyse des tendances du marché
- Après la recherche, l'application affiche une analyse des tendances du marché pour la ville sélectionnée.

---

## Documentation des fichiers

### `main.py`
- **Rôle** : Point d'entrée de l'application.
- **Fonctionnalités** :
  - Importe et exécute la fonction `main()` de `ui/app.py`.

### `models/schemas.py`
- **Rôle** : Définit les schémas de données pour la validation.
- **Classes** :
  - `PropertyData` : Schéma pour les données d'une propriété.
  - `PropertiesResponse` : Schéma pour une réponse contenant plusieurs propriétés.
  - `LocationData` : Schéma pour les tendances des prix par localité.
  - `LocationsResponse` : Schéma pour une réponse contenant plusieurs localités.
  - `FirecrawlResponse` : Schéma pour la réponse de l'API Firecrawl.

### `services/property_agent.py`
- **Rôle** : Contient la logique métier de l'agent de recherche de propriétés.
- **Classes** :
  - `PropertyFindingAgent` : Agent responsable de la recherche et de l'analyse des propriétés.
    - **Méthodes** :
      - `find_properties()` : Recherche des propriétés en fonction des critères de l'utilisateur.
      - `get_location_trends()` : Analyse les tendances du marché pour une ville donnée.

### `utils/config.py`
- **Rôle** : Gère la configuration de l'application (clés API, etc.).
- **Fonctions** :
  - `setup_api_keys()` : Configure les clés API dans l'état de session Streamlit.

### `ui/app.py`
- **Rôle** : Contient la logique de l'interface utilisateur avec Streamlit.
- **Fonctions** :
  - `setup_page()` : Configure la page Streamlit et ajoute du CSS personnalisé.
  - `setup_sidebar()` : Configure la barre latérale pour la saisie des clés API.
  - `main_interface()` : Affiche l'interface principale pour la recherche de propriétés.
  - `main()` : Point d'entrée de l'interface utilisateur.

---

## Personnalisation
- **CSS** : Vous pouvez personnaliser le style de l'application en modifiant le CSS dans `ui/app.py`.
- **Fonctionnalités** : Ajoutez de nouvelles fonctionnalités en étendant les classes dans `services/property_agent.py`.