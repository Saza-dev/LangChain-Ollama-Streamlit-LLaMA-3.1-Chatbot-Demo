# 🦙 LangChain + Ollama + Streamlit: LLaMA 3.1 Chatbot Demo

A minimal chatbot demo that integrates **LangChain**, **Ollama**, and **Streamlit** to run **Meta's LLaMA 3.1** model locally. This app accepts a user question, sends it through a LangChain prompt pipeline, and returns a response powered by LLaMA 3.1.

---

## 🔧 Tech Stack

- **Python**
- **LangChain**
- **Ollama** (for running LLaMA 3.1 locally)
- **Streamlit** (for the UI)
- **dotenv** (for environment variable management)
- **LangSmith** (for tracing/debugging LangChain pipelines)

---

## 🚀 Getting Started

1. Clone the repository:
 ```
https://github.com/Saza-dev/LangChain-Ollama-Streamlit-LLaMA-3.1-Chatbot-Demo.git
 ```
2. Install Dependencies:
   Make sure you’re using Python 3.9 or later.
  ```
pip install -r requirements.txt
  ```
3. Setup Environment Variables
   Create a .env file in the project root:
 ```
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_project_name
 ```
4. Install and Run Ollama with LLaMA 3.1
```
ollama run llama3.1
```
5. Run the App
```
streamlit run app.py
```
