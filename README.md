# Enterprise RAG Chatbot
An enterprise-grade Retrieval-Augmented Generation (RAG) chatbot that enables users to upload company documents and receive context-aware answers using Large Language Models.
> Currently under active development.
---
## Project Overview
This project implements a scalable RAG pipeline that processes PDF documents, converts them into semantic embeddings, stores them in Pinecone Vector Database, and retrieves the most relevant information during user queries.
The goal is to build a production-ready AI assistant capable of answering questions from private company knowledge bases instead of relying only on an LLM's pretrained knowledge.
---
## Features Implemented
• Upload PDF documents
• Automatically split PDFs into semantic chunks
• Generate embeddings using Sentence Transformers
• Store embeddings in Pinecone
• Retrieve relevant document chunks using similarity search
• Generate grounded answers with Gemini
• Prompt engineering to reduce hallucinations
• FastAPI REST API
---
## Tech Stack
### Backend
- Python
- FastAPI
### AI / LLM
- LangChain
- Hugging Face Embeddings
- Google Gemini (planned)
### Vector Database
- Pinecone
### Document Processing
- PyPDFLoader
- RecursiveCharacterTextSplitter
---
## Project Structure
PDF Upload
      ↓
Load PDF
      ↓
Recursive Chunking
      ↓
Generate Embeddings
      ↓
Store in Pinecone
      ↓
User asks a question
      ↓
Similarity Search
      ↓
Retrieve Top-k Chunks
      ↓
Gemini generates answer
---
## Upcoming Features
- PDF Upload API
- Semantic Retrieval
- Gemini-powered Question Answering
- Conversation Memory
- React / Next.js Frontend
- Production Deployment
---
## Learning Goals
This project is being built to gain hands-on experience with:
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Embedding Models
- LLM Application Development
- FastAPI
- Production AI Systems
---

##Status
Current Progress

✅ PDF Upload API
✅ PDF Ingestion
✅ Recursive Chunking
✅ Sentence Transformer Embeddings
✅ Pinecone Vector Database
✅ Semantic Retrieval
✅ Gemini-powered Question Answering
✅ FastAPI Backend

🚧 React / Next.js Frontend
🚧 Conversation Memory
🚧 Streaming Responses
🚧 Authentication
🚧 Production Deployment
---
## Author
Jasmeet Kaur
Computer Science Engineering (AI & ML)
Building production-ready AI applications while learning LLM Engineering.
