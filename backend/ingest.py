from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings

from pinecone import Pinecone, ServerlessSpec

load_dotenv()   

from vectorstore import vectorstore


def ingest_pdf(pdf_path):
    
    loader = PyPDFLoader(pdf_path)
    
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
        )
    
    chunks = text_splitter.split_documents(documents)
    
    vectorstore.add_documents(chunks)
    
    print("Documents uploaded successfully!!!!!!!")
    
    return len(chunks)


'''
index = pc.Index("enterprise_demo")

vectorstore = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

vectorstore uses pinecone indirectly here to convert chunks into embeddings
and then upload them to the index
'''


