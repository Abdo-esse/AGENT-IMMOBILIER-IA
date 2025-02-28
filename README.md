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