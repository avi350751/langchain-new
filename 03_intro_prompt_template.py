import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

prompt_template = PromptTemplate(
    input_variables=["country","no_of_paras","language"],
    template ="""
    You are a travel guide. You are expert in traditional cuisines.
    You provide information about specific dish from specific country.
    
    Answer the question: What is the traditional cuisine of {country}?
    Provide the answer in {no_of_paras} short paragraphs in {language}."""
)

st.title("Traditional Cuisine Information")

country = st.text_input("Enter the country: ")
no_of_paras = st.number_input("Number of paras: ",min_value=1, max_value=5)
language = st.text_input("Enter the preferred language: ")
if country:
    response = llm.invoke(prompt_template.format(country=country, no_of_paras=no_of_paras, language=language)).content
    st.write("Response: ", response)
