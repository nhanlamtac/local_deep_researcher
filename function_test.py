from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
from src.ollama_deep_researcher.task_pdf import get_abstract

file_path = "Paper/SGE_net_Video_object_detection_with_squeezed_GRU_and_information_entropy_map.pdf"
loader = PyPDFLoader(
    file_path = file_path,
    # headers = None
    # password = None,
    mode = "single"
)

# pages = []
pages = loader.load()
# pull exactly one page
# try:
#     first_page = next(pages_lazy)
#     pages.append(first_page)
# except StopIteration:
#     # PDF was empty or no pages to load
#     pass
# for page in pages_lazy:
#     for i in range(1, 2):
#         pages.append(page)
print(f"{pages[0].metadata}\n")
# print(f"{pages[0].metadata['author']}\n")
print(f"{pages[0].metadata['title']}\n")
abstract = get_abstract(file_path=file_path)
print(abstract)
# splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# chunks = splitter.split_documents(pages)
# print(chunks[0].page_content)
# embeddings = OpenAIEmbeddings()
# vector_store = InMemoryVectorStore.from_documents(chunks[0], embeddings)
# qa = RetrievalQA.from_llm(llm=OpenAI(temperature=0), retriever=vector_store.as_retriever())

# paper = qa.run("What is the title of this paper?")
# abstract = qa.run("What is the abstract of this paper?")
# print(paper)
# print(abstract)
# print(pages[0].page_content)
# pages2 = pages[0].page_content[:10000]
# vector_store = InMemoryVectorStore.from_documents(pages, OpenAIEmbeddings())
# docs = vector_store.similarity_search("Abstract", k=2)
# for doc in docs:
#     print(f'Page {doc.metadata["page"]}: {doc.page_content[:300]}\n')

