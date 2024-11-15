import git
import os
import pickle

from queue import Queue
local = False
if local:
    from dotenv import load_dotenv
    load_dotenv()

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain_community.vectorstores import FAISS 
from langchain_community.embeddings import HuggingFaceEmbeddings
model_name = "sentence-transformers/all-MiniLM-L6-v2"#
model_kwargs = {"device": "cuda"}
# openaimodel = "gpt-3.5-turbo-0125" #"gpt-4o-mini-2024-07-18" gpt-4o-2024-08-06
allowed_extensions = ['.py', '.ipynb', '.md']
import uuid

from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.storage import InMemoryByteStore
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import HuggingFacePipeline
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter,RecursiveCharacterTextSplitter

import localllm

class Embedder:
    def __init__(self, path) -> None:
        # self.git_link = git_link
        # last_name = self.git_link.split('/')[-1]
        # self.clone_path = last_name.split('.')[0]
        # self.model = localllm.create_localllm(model_id="meta-llama/Meta-Llama-3.1-8B-Instruct")#ChatOpenAI(model_name=openaimodel)  # switch to 'gpt-4'
        self.hf = HuggingFaceEmbeddings(model_name=model_name)
        self.file_path = path


  
    def chunk_files(self):

        loader = TextLoader( self.file_path, encoding = 'UTF-8')
        self.docs = loader.load()
        large_text = self.docs[0].page_content
    
        def python_function_splitter(text):
            """Splits text into each function"""
            chunks = []
            current_chunk = ""
            indent_level = 0
            for line in text.splitlines():
                current_chunk += line + "\n"
                if line.strip().startswith("def "):  # Start of a function
                    indent_level += 1
                elif line.strip().startswith("}"):# and indent_level > 0:  # a line only have }
                    indent_level -= 1
                    if indent_level == 0:  # End of function
                        chunks.append(current_chunk)
                        # print("\ncurrent chunk:",current_chunk)
                        current_chunk = ""
                # print("Line:",line)
                # print("indent_level:",indent_level)
            if current_chunk:
                
                chunks.append(current_chunk)  # Add the last chunk if exists
            return chunks

        split_docs = python_function_splitter(large_text)

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
        self.texts = text_splitter.create_documents(split_docs)

        self.num_texts = len(self.texts)



    def embed_Chroma(self):
        vectorstore = Chroma(
            collection_name="full_documents", embedding_function=self.hf
        )

        return vectorstore

    def embed_FAISS(self):
        db = FAISS.from_documents(self.texts, embedding= self.hf)
        # local_db_path = "./scene_rag/"
        # # self.delete_directory(self.clone_path)
        # os.makedirs(local_db_path, exist_ok=True)

        # # Step 6: Save the FAISS index locally
        # db.save_local(local_db_path)
        return db
        
    def load_db(self):
            ## Create and load
        print("loading database for RAG")

        self.chunk_files()

