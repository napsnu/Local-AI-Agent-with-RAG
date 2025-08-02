import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about a pizza restaurant.
Here are some relevant reviews:{reviews}
Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

st.title("Pizza Restaurant Q&A")

question = st.text_input("Ask your question about the pizza restaurant:")

if question:
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    st.write(result)