# 🧠 AI-Agent powered by Langchain & Ollama

Un agent intelligent capable de répondre à des questions à partir d’avis utilisateurs, propulsé par **Langchain**, **Ollama**, et **Llama3**. Le projet utilise aussi **ChromaDB** comme base vectorielle pour rechercher les avis les plus pertinents.

---

## 🚀 Fonctionnalités

- 🤖 Génération de réponses avec LLM (`llama3`)
- 🔍 Recherche sémantique d’avis avec ChromaDB
- 📄 Traitement d’un fichier CSV contenant des avis de restaurants
- 🧩 Modularité pour intégrer d'autres modèles ou bases vectorielles
- 🧠 Embeddings générés avec `mxbai-embed-large`

---

## 📁 Structure du projet

AI-agent/
├── main.py                       # Code principal de l’agent conversationnel

├── vector.py                     # Script pour créer et alimenter la base vectorielle Chroma

├── realistic_restaurant_reviews.csv  # Données d’entrée (avis de restaurants)

├── README.md                     # Fichier de documentation

├── requirements.txt              # Dépendances du projet

└── chrome_langchain_db/          # Base vectorielle persistée localement

---

## 🔧 Installation

### 1. Cloner le dépôt

### 2. Créer et activer un environnement virtuel
python -m venv venv
venv\Scripts\activate  # Windows

### 3. Installer les dépendances
pip install -r requirements.txt

Ou individuellement : pip install langchain langchain-community langchain-ollama chromadb pandas
⚠️ Si chromadb échoue à s’installer, installe Visual C++ Build Tools puis relance.

## 🧠 Utilisation
### 1. Démarrer Ollama et télécharger le modèle
ollama run llama3
ou
ollama pull llama3

### 2. Générer les embeddings
python vector.py

### 3. Lancer l’agent
python main.py


## ✅ Exemple de question
Question : What is the best pizza place in New York?

Réponse générée : Joe’s Pizza is the top contender with its crispy crust and flavorful sauce...
