from fastapi import FastAPI, UploadFile, File
import shutil
import os

from backend.ingest import ingest_pdf

from backend.chatbot import generate_answer

from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str

app =  FastAPI()

@app.get("/")
def home():
    return{"message":"Welcome to Enterprise RAG Chatbot!"}

@app.post("/upload")
def upload_pdf(pdf: UploadFile = File(...)):
    upload_folder = "data/pdfs"
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder,pdf.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(pdf.file, buffer)
    chunks = ingest_pdf(file_path)
    
    return{
        "message": "PDF uploaded successfully!",
        "filename" : pdf.filename,
        "chunks_created" : chunks
    }
    
@app.post("/chat")
def chat(request: ChatRequest):

    answer = generate_answer(request.query)

    return {
        "query": request.query,
        "answer": answer
    }
    
