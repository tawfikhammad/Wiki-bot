from langchain.text_splitter import CharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def build_search_index(source):
    source_chunks = []

    splitter = CharacterTextSplitter(separator=" ", chunk_size=1024, chunk_overlap=0)

    for chunk in splitter.split_text(source.page_content):
            source_chunks.append(Document(page_content=chunk, metadata=source.metadata))

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_documents(source_chunks, embeddings)