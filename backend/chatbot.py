from dotenv import load_dotenv
load_dotenv()

from backend.vectorstore import vectorstore
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


def generate_answer(query):

    docs = vectorstore.similarity_search(query, k=5)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
    You are an AI assistant that answers questions about the uploaded documents.

    Rules:
    - Answer ONLY from the provided context.
    - If the answer is not present in the context, reply:
    "I couldn't find that information in the uploaded document."
    - Do not make up facts.
    - Keep the answer clear, concise, and well formatted.
    - If possible, answer using bullet points.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    response = llm.invoke(prompt)

    return response.content
    
