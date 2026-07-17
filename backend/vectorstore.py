from dotenv import load_dotenv
import os

from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = "college-handbook"
    
if index_name not in pc.list_indexes().names():
        (
            pc.create_index(
                name = index_name,
                dimension = 384,
                metric = "cosine",
                spec = ServerlessSpec(
                    cloud = "aws",
                    region = "us-east-1"
                )
            )
        )
        
print("Index Ready!!!!!!!!!!!!!!!!!!")

index = pc.Index("college-handbook")


vectorstore = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

