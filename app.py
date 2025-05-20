import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

# langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assitant. Please response to the question asked"),
        ("user","Question:{question}")
    ]
)

# Streamlit ramework
st.title("Langachain Demo With LLAMA3.1")
input_text = st.text_input("What question you have in mind?")


# Ollama Llama3.1 model
llm = Ollama(model="llama3.1")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

