from dotenv import load_dotenv
load_dotenv()
from vectorstore import vectorstore
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

query = "What is the criteria for passing?"

docs = vectorstore.similarity_search(query, k=3)

context = "\n\n".join(doc.page_content for doc in docs)    

prompt = f"""

You are a helpful assistant. 

Answer the question using ONLY the provided context.

context = {context}

query = {query}

"""
response = llm.invoke(prompt)
print(response.content)