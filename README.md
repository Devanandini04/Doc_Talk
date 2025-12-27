# Doc_Talk 📄

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![OpenAI](https://img.shields.io/badge/API-OpenAI%2FGoogle-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Doc_Talk** is a sophisticated RAG-based (Retrieval-Augmented Generation) application designed to bridge the gap between static PDF documents and interactive AI conversations. It allows users to query their documents in natural language and receive accurate, context-aware responses.

## 🧠 How It Works
The application follows a standard RAG pipeline:
1. **Load:** PDF text is extracted.
2. **Split:** Text is divided into smaller, manageable chunks.
3. **Embed:** Chunks are converted into vector embeddings (using OpenAI or Google Gemini).
4. **Store:** Vectors are stored in a local FAISS database.
5. **Retrieve & Generate:** Relevant chunks are retrieved based on the user's question and passed to the LLM to generate an answer.

## 🚀 Key Features
- **📄 Multi-Document Support:** Upload and process multiple PDFs simultaneously.
- **🔍 Semantic Search:** Uses FAISS vector store for high-accuracy similarity search.
- **🤖 LLM Integration:** Powered by LangChain with support for OpenAI (GPT) or Google Gemini.
- **💬 Interactive UI:** Clean and responsive chat interface built with Streamlit.
- **⚡ Cost-Effective:** Optimized token usage for embeddings.

## 🛠️ Tech Stack
| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit |
| **Orchestration** | LangChain |
| **Embeddings** | OpenAI / Google Generative AI |
| **Vector Store** | FAISS (Facebook AI Similarity Search) |
| **Language** | Python |

## 📦 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/Devanandini04/Doc_Talk.git](https://github.com/Devanandini04/Doc_Talk.git)
   cd Doc_Talk