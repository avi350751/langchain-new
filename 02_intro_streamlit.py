import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

st.title("Ask Anything..")
question = st.text_input("Enter your question here: ")
if question:
    response = llm.invoke(question).content
    st.write("Response: ", response)
