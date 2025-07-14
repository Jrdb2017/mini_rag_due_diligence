# 📄 Mini RAG Due Diligence Q&A

A small demo project to showcase Python, FastAPI, Retrieval-Augmented Generation (RAG), vector search, and a Next.js frontend — inspired by AI-driven due diligence systems like Keye.

---

## 🚀 Features

✅ Ingest multiple "deal room" docs (sample .txt files)  
✅ Split & embed using LangChain + FAISS vector store  
✅ FastAPI backend exposes `/ask` endpoint  
✅ Next.js frontend to submit questions and show answers  
✅ Containerized using Docker & orchestrated with Docker Compose

---

## ⚙️ Tech Stack

- **Backend:** Python, FastAPI, LangChain, FAISS
- **Frontend:** Next.js (React)
- **Vector Store:** FAISS
- **Deployment:** Docker, Docker Compose


To run add a .env file in the root directory with an open ai api key
OPENAI_API_KEY=...

Then with docker running, run this command: *docker-compose up --build* and then visit http://localhost:3000
