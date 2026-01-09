import streamlit as st
import tempfile
from pathlib import Path
import json

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.

def get_financial_data(file_path):
    """
    Extracts financial data from a PDF file.
    """
    # Load Documents
    loader = PyPDFLoader(str(file_path))
    docs = loader.load()

    # Split
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # Embed
    vectorstore = Chroma.from_documents(documents=splits, 
                                        embedding=OpenAIEmbeddings())

    retriever = vectorstore.as_retriever()

    # Prompt
    template = """
    You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. 
    If you don't know the answer, just say that you don't know. 
    Use three sentences maximum and keep the answer concise and extract only the value.
    Question: {question} 
    Context: {context} 
    Answer:
    """
    prompt = ChatPromptTemplate.from_template(template)
    
    # LLM
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # Post-processing
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # Base RAG chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # Define the questions for each metric
    questions = {
        "total_assets": "What is the value for 'Total Assets' for the most recent fiscal year from the 'Consolidated Balance Sheets'?",
        "total_liabilities": "What is the value for 'Total Liabilities' for the most recent fiscal year from the 'Consolidated Balance Sheets'?",
        "net_sales": "What is the value for 'Net Sales' for the most recent fiscal year from the 'Consolidated Statements of Operations'?",
        "net_income": "What is the value for 'Net Income' for the most recent fiscal year from the 'Consolidated Statements of Operations'?"
    }

    # Define the parallel chains to run for each question
    map_chain = RunnableParallel(
        total_assets=(lambda x: x["total_assets"]) | rag_chain,
        total_liabilities=(lambda x: x["total_liabilities"]) | rag_chain,
        net_sales=(lambda x: x["net_sales"]) | rag_chain,
        net_income=(lambda x: x["net_income"]) | rag_chain,
    )

    # Invoke the parallel chains with the questions dictionary
    result = map_chain.invoke(questions)
    
    return result

st.set_page_config(page_title="Financial Data Extractor", layout="wide")

st.title("Financial Data Extractor from PDF")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = Path(tmp_file.name)

    if st.button("Extract Financial Data"):
        with st.spinner("Extracting data... This may take a moment."):
            try:
                financial_data = get_financial_data(tmp_file_path)
                st.success("Extraction complete!")
                st.json(financial_data)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    
    # Clean up the temporary file
    if 'tmp_file_path' in locals() and tmp_file_path.exists():
        tmp_file_path.unlink()
