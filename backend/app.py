from fastapi import FastAPI

app =  FastAPI()

@app.get("/")
def home():
    return{"message":"Welcome to Enterprise RAG Chatbot!"}

from fastapi import FastAPI, UploadFile, File

@app.post("/upload")
def upload_pdf(pdf: UploadFile = File(...)):
    return{
        "filename": pdf.filename,
        "content_type": pdf.content_type    
    }
  