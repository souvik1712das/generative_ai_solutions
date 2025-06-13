# 🧠 ElasticMind
ElasticMind is a Local AI Assistant that blends Elasticsearch vector search, local LLMs (via Ollama), and RAG (Retrieval-Augmented Generation) to semantically search and answer questions from your uploaded files — all locally, with full data control.

🧩 Tagline
ElasticMind – Where Questions Meet Context — with RAG & Local LLMs

🔥 Key Features

✅ Upload CSV or TXT files and embed their contents semantically

🔍 Store embeddings in Elasticsearch using dense vector indexing

🧠 Use Ollama-hosted local models to generate answers with context

❓ Ask natural language questions; retrieve relevant chunks from Elasticsearch

📋 Easily switch between or create new indices interactively in the UI

⚙️ Installation Requirements

📦 1. Install Python Environment

python -m venv .venv
source .venv/bin/activate         # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

🔍 2. Install & Run Elasticsearch (8.x)

Download from: https://www.elastic.co/downloads/elasticsearch

Extract and run: bin/elasticsearch

✅ Ensure Elasticsearch is running on http://localhost:9200 and allows dense_vector indexing.

🧠 3. Install & Run Ollama

ollama run mistral
ollama run mxbai-embed-large

📊 4. (Optional) Install Kibana for ES Dashboarding

 Download from: https://www.elastic.co/downloads/kibana

Extract and run: bin/kibana

🚀 How to Run the App

streamlit run "ElasticMind.py"


📁 Folder Structure

├── ElasticMind.py      # Streamlit app (ElasticMind UI)

├── requirements.txt               # All dependencies

└── README.md                      # This file

📊 Example Use Cases

🔁 Fintech logs: Query transaction failures, suspicious patterns from bank API logs

📜 Clinical Query Assistant for Medical Investigators: Helps non-technical clinical experts get insights from massive datasets via chat.

📄 Policy & SOP documents: Ask natural questions over operational or compliance docs

📜 Audit logs: Semantic search over error trails or historical records

🧑‍💻 Support tickets: Summarize and retrieve similar tickets from past support queries

🧾 Product manuals: Find relevant sections of documentation with one-line queries

🧠 How It Works

Embed Data

Upload a file → Embed rows/lines via Ollama (mxbai-embed-large) → Store as dense_vector in Elasticsearch

Ask a Question

Input a natural language question → Embed → Match top documents via cosine similarity

Answer Generation (RAG)

Top documents passed as context → Mistral generates a response

⚙️ Note: The solution is currently in its very early stage and still evolving. There's plenty of scope for improving response accuracy, query interpretation, and overall robustness. Feedback and contributions are welcome!

🛣️ Future Improvements

 Query interpretation and response accuracy

 Hybrid (keyword + vector) search
 
 Chat history & memory
 
 File format support for PDFs, DOCX

 🙏 Acknowledgements

Thanks to:

Ollama

Elasticsearch

Langchain

Streamlit

Also to ChatGPT and Gemini for continuous support

Author: Souvik Das | Last updated: 13 June 2025

# EDITS

13062025: Content has been updated.
