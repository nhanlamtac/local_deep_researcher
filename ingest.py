import sys
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM

from langchain.embeddings import HuggingFaceEmbeddings

def ingest(file_path, persist_dir="db"):
    load_dotenv()
    loader = PyPDFLoader(file_path)
    # docs = loader.load()
    # print(docs)
    docs = loader.load_and_split()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    vectordb.persist()
    print(f"Ingested {len(docs)} chunks from {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ingest.py path/to/your_paper.pdf")
    else:
        ingest(sys.argv[1])

