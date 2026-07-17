from dotenv import load_dotenv
load_dotenv()

from backend.vectorstore import vectorstore

query = "What is the criteria for pass marks?"

docs = vectorstore.similarity_search(query, k=3)

for i, doc in enumerate(docs, start=1):
    print(f"\n---------- Result {i} ----------\n")
    print(doc.page_content)
    
