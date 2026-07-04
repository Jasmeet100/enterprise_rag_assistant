# Enterprise RAG Chatbot
An enterprise-grade Retrieval-Augmented Generation (RAG) chatbot that enables users to upload company documents and receive context-aware answers using Large Language Models.
> Currently under active development.
---
## Project Overview
This project implements a scalable RAG pipeline that processes PDF documents, converts them into semantic embeddings, stores them in Pinecone Vector Database, and retrieves the most relevant information during user queries.
The goal is to build a production-ready AI assistant capable of answering questions from private company knowledge bases instead of relying only on an LLM's pretrained knowledge.
---
## Features Implemented
- PDF document ingestion
- Document loading using LangChain
- Recursive text chunking
- Semantic embeddings using Sentence Transformers
- Pinecone Vector Database integration
- Automatic vector storage
- Modular project architecture
- FastAPI backend setup (In Progress)
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
backend/
│
├── app.py
├── ingest.py
├── vectorstore.py
│
data/
└── pdfs/
│
.env
requirements.txt
---
## Current Workflow
PDF Upload
↓
Load PDF
↓
Split into Chunks
↓
Generate Embeddings
↓
Store Embeddings in Pinecone
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
## Status
Current Progress:
- PDF Ingestion ✅
- Chunking ✅
- Embeddings ✅
- Pinecone Integration ✅
- FastAPI Backend 🚧
- Retrieval Pipeline ⏳
- Chat Interface ⏳
- Deployment ⏳
---
## Author
Jasmeet Kaur
Computer Science Engineering (AI & ML)
Building production-ready AI applications while learning LLM Engineering.
