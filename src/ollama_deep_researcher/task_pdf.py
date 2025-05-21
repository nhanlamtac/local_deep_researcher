#!/usr/bin/env python3
import sys
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.vectorstores import InMemoryVectorStore
from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.llms import LlamaCpp
# from langchain.chains import RetrievalQA
import re

def ingest(file_path):
    load_dotenv()
    loader = PyPDFLoader(file_path)
    pages = []
    docs = loader.load()
    # Embed and store in‐memory
    paper = docs[0].metadata['title']
#    abstract = docs[0].metadata['author']
    return paper

def get_abstract(file_path):
    # Load PDF
    loader = PyPDFLoader(file_path=file_path)
    docs = loader.load()  # full pages as Documents
    first_page = docs[0].page_content
    text = first_page.replace("-\n", " ")
    text = " ".join(text.split())
    pattern = r"abstract[:\s]*(.*?)(?=\n[A-Z][A-Za-z ]+\n|1. Introduction)"
    m = re.search(pattern, text, flags=re.S | re.I)
    if m:
        raw_abstract = m.group(1).strip()
    else:
        raw_abstract = first_page  # fallback: just send whole page
    return raw_abstract


def summary_pdf():
    pass

def compare_pdf():
    pass

def extract_pdf_name(s: str) -> str | None:
    for token in s.split():
        if token.lower().endswith('.pdf'):
            return token
    return None


import sqlite3

def upload_pdf_f(research_topic: str):
    file_path = extract_pdf_name(research_topic)
    paper = ingest(file_path=file_path)
    abstract = get_abstract(file_path=file_path)
    source = "internal"
    # Add to the database
    conn = sqlite3.connect('papers.db')
    c = conn.cursor()
    c.execute("INSERT INTO papers (title, abstract, source) VALUES (?, ?, ?)", (paper, abstract, source))
    conn.commit()
    conn.close()
    return paper, abstract


