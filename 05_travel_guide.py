import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

prompt_template = PromptTemplate(
    input_variables=["city","month","language","budget"],
    template ="""
    Welcome to the {city} travel guide.
    If you're visiting in {month}, here's what you can do:
    1. Must-visit attractions
    2. Local cuisine you must try
    3. Useful phrases in {language}
    4. Tips for travelling on a {budget} budget.
    
    Enjoy your trip!"""
)

st.title("Travel Companion!")
city = st.text_input("Enter the city you are visiting:")
month = st.text_input("Enter the month of your visit:")
language = st.text_input("Enter the local language spoken there:")
budget = st.selectbox("Enter your budget ",["low","medium","high"])

if st.button("Get Travel Tips"):
    if city and month and language and budget:
        prompt = prompt_template.format(
            city = city,
            month=month,
            budget=budget,
            language=language)
        response = llm.invoke(prompt).content
        st.subheader("Your travel guide: ")
        st.write(response)
    else:
        st.error("Please fill in all the fields.")