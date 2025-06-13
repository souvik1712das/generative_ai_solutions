# 🧠 ElasticMind
ElasticMind is a Local AI Assistant that blends Elasticsearch vector search, local LLMs (via Ollama), and RAG (Retrieval-Augmented Generation) to semantically search and answer questions from your uploaded files — all locally, with full data control.

🧩 **Tagline**
ElasticMind – Where Questions Meet Context — with RAG & Local LLMs

🔥 **Key Features**

✅ Upload CSV or TXT files and embed their contents semantically

🔍 Store embeddings in Elasticsearch using dense vector indexing

🧠 Use Ollama-hosted local models to generate answers with context

❓ Ask natural language questions; retrieve relevant chunks from Elasticsearch

📋 Easily switch between or create new indices interactively in the UI

****Demo****
[ElasticMind.webm](https://github.com/user-attachments/assets/c9ae7678-f78a-4568-815d-b1c709407a8b)

**A few Trials**

![image](https://github.com/user-attachments/assets/a677ae57-250f-43de-8522-a44a9e1299ab) 

![image](https://github.com/user-attachments/assets/53520564-4324-416f-a134-d6dec99e77ea)


⚙️ **Installation Requirements**

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

🚀 **How to Run the App**

streamlit run "ElasticMind.py"


📁 **Folder Structure**

├── ElasticMind.py      # Streamlit app (ElasticMind UI)

├── requirements.txt               # All dependencies

└── README.md                      # This file

📊 **Example Use Cases**

📜 Clinical Query Assistant for Medical Investigators: Helps non-technical clinical experts get insights from massive datasets via chat.

📄 Policy & SOP documents: Ask natural questions over operational or compliance docs

📜 Audit logs: Semantic search over error trails or historical records

🧑‍💻 Support tickets: Summarize and retrieve similar tickets from past support queries

🧾 Product manuals: Find relevant sections of documentation with one-line queries

🧾 Custom document search engine

🔁 Fintech logs: Query transaction failures, suspicious patterns from bank API logs



🧠 **How It Works**

Embed Data

Upload a file → Embed rows/lines via Ollama (mxbai-embed-large) → Store as dense_vector in Elasticsearch

Ask a Question

Input a natural language question → Embed → Match top documents via cosine similarity

Answer Generation (RAG)

Top documents passed as context → Mistral generates a response

⚙️ **Note**: _The solution is currently in its very early stage and still evolving. There's plenty of scope for improving response accuracy, query interpretation, and overall robustness. Feedback and contributions are welcome!_

🛣️ **Future Improvements**

 Query interpretation and response accuracy

 Indexing rows as a textual narrative for a tabular dataset

 Hybrid (keyword + vector) search
 
 Chat history & memory
 
 File format support for PDFs, DOCX

 🙏 **Acknowledgements**

Thanks to:

Ollama

Elasticsearch

Langchain

Streamlit

Also to ChatGPT and Gemini for continuous support

**Author**: Souvik Das | **Last updated**: 13 June 2025 | **LinkedIn**: https://www.linkedin.com/in/souvik-das-6ba904a2/

# EDITS

13062025: Initial version published.
