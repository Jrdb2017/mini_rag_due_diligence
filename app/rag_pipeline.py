from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA
from data_load import load_documents
import os

class RAGPipeline:
    def __init__(self):
        self.docs = load_documents()
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        self.chunks = self._split_docs(self.docs)
        self.embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True}
        )
        self.vectorstore = FAISS.from_texts(self.chunks, self.embeddings)
        self.qa = RetrievalQA.from_chain_type(
            llm=OpenAI(temperature=0),
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever()
        )

    def _split_docs(self, docs):
        chunks = []
        for doc in docs:
            chunks.extend(self.text_splitter.split_text(doc))
        return chunks

    def answer_question(self, question):
        return self.qa.run(question) 