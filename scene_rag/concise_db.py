
import utils_rag
import time
import os
import re
import warnings
import localllm
import logging
import pickle   
import sys
from tqdm import tqdm
from operator import itemgetter
import uuid

from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain.storage import InMemoryByteStore

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ChatMessageHistory
from langchain_community.vectorstores import FAISS, Chroma
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.text_splitter import CharacterTextSplitter,RecursiveCharacterTextSplitter
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.documents import Document
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
    FewShotPromptTemplate
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import argparse

# Suppress all warnings
warnings.filterwarnings("ignore")

def main():
    parser = argparse.ArgumentParser(description="Run different models based on command-line flags.")
    
    parser.add_argument(
        '--model', 
        choices=['llama', 'mistral', 'gpt'], 
        required=True, 
        help="Specify the model to run. Choices are: 'llama', 'mistral', 'gpt'  ."
    )

    args = parser.parse_args()

    print("Creating llm...")

    if args.model == 'mistral':
        
        model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
        print("Using ",model_id)
        model = localllm.create_localllm(model_id=model_id)
        
    elif args.model == 'llama':
        
        model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
        print("Using ",model_id)
        model = localllm.create_localllm(model_id=model_id)
        
    else:
        print("Using gpt from openai") 
        model = ChatOpenAI(model_name="gpt-4o-mini-2024-07-18",openai_api_key='OPENAI_KEY')
          #gpt-4o-mini, gpt-3.5-turbo-0125 gpt-4o-2024-08-06,gpt-4o-mini-2024-07-18
   
    file = "/processed_snake.txt"

    embedder = utils_rag.Embedder(file)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    ## Chunk and Create DB
    


    # ##include chat history
    # contextualize_q_system_prompt = """Given a chat history and the latest user question \
    # which might reference context in the chat history, formulate a standalone question \
    # which can be understood without the chat history and don't change the mearning of the latest user question. Do NOT answer the question, \
    # just reformulate it if needed and otherwise return it as is."""
    # contextualize_q_prompt = ChatPromptTemplate.from_messages(
    #     [
    #         ("system", contextualize_q_system_prompt),
    #         MessagesPlaceholder("chat_history"),
    #         ("human", "{input}"),
    #     ]
    # )
    # history_aware_retriever = create_history_aware_retriever(
    #     model, embedder.retriever, contextualize_q_prompt
    # )



    # This is a prompt template used to format each individual example.
    # example_prompt = ChatPromptTemplate.from_messages(
    #     [
    #         ("human", "{description}"),
    #         ("ai", "{command}"),
    #     ]
    # )
    # few_shot_prompt = FewShotChatMessagePromptTemplate(
    #     example_prompt=example_prompt,
    #     examples=examples,
    # )

 # Focus primarily on "spawn_placeholder" objects and extract useful information from the provided context
    qa_system_prompt = """You are a good assistant in extracting informations from code-like text input. You will be given several code segments about the same blender scene. You should understand this Blender usda scene, extract useful information, and output formated and concise context which includes all information.\
    Keep the answer concise.  \
    You should output a list of dict format text summary that will faithfully describe each object in the scene.\  
    You can include more keys and informations if they appears in the "def Xform" as parameters. DO NOT provide any explanations. DO NOT ask questions.\
        Example:
        context: def Xform "BushFactory_1090821408__spawn_placeholder_0_"
                {{
                    matrix4d xformOp:transform = NUM
                    uniform token[] xformOpOrder = ["xformOp:transform"]

                    def Xform "Tree_006"
                    {{
                        matrix4d xformOp:transform = NUM
                        uniform token[] xformOpOrder = ["xformOp:transform"]
                    }}
                }}

                def Xform "BushFactory_1090821408__spawn_placeholder_1_"
                {{
                    matrix4d xformOp:transform = NUM
                    uniform token[] xformOpOrder = ["xformOp:transform"]

                    def Xform "Tree_007"
                    {{
                        matrix4d xformOp:transform = NUM
                        uniform token[] xformOpOrder = ["xformOp:transform"]
                    }}
                }}

                def Xform "CameraRigs_0_0"
                {{
                    matrix4d xformOp:transform = NUM
                    uniform token[] xformOpOrder = ["xformOp:transform"]

                    def Camera "Camera_001"
                    {{
                        float2 clippingRange = (0.1, 10000)
                        float focalLength = 35.19107
                        float horizontalAperture = 32
                        float horizontalApertureOffset = 0
                        token projection = "perspective"
                        float verticalAperture = 18
                        float verticalApertureOffset = 0
                    }}
                }}
                
                def Xform "animhelper_SnakeFactory_1090821408__create_placeholder_0__p"
                {{
                    matrix4d xformOp:transform = NUM 
                uniform token[] xformOpOrder = ["xformOp:transform"]

                    def BasisCurves "animhelper_SnakeFactory_1090821408__create_placeholder_0__p"
                    {{
                        int[] curveVertexCounts = NUM 
                point3f[] points = NUM 
                uniform token type = "linear"
                        float[] widths = NUM 
                interpolation = "vertex"
                        )
                        uniform token wrap = "nonperiodic"
                    }}

                    def Xform "animhelper_SnakeFactory_1090821408__create_placeholder_0__path"
                    {{
                        matrix4d xformOp:transform = NUM 
                uniform token[] xformOpOrder = ["xformOp:transform"]

                        def NurbsCurves "policy_path_curve"
                        {{
                            int[] curveVertexCounts.timeSamples = NUM 
                double[] knots.timeSamples = NUM 
                int[] order.timeSamples = NUM 
                point3f[] points.timeSamples = NUM 
                float[] widths (
                                interpolation = "vertex"
                            )
                            float[] widths.timeSamples = NUM 
                }}
                def Xform "Empty"
                {{
                    matrix4d xformOp:transform = NUM 
                uniform token[] xformOpOrder = ["xformOp:transform"]
                }}

                def Xform "OpaqueTerrain_unapplied"
                {{
                    matrix4d xformOp:transform = NUM 
                uniform token[] xformOpOrder = ["xformOp:transform"]
                }}

                


        assistant:
            [
                {{
                    name: "BushFactory(1090821408).spawn_placeholder(0)",
                    type: "Xform",
                    variables: "transform",
                    children: [{{
                        name: "Tree.006",
                        type: "Xform",
                        variable: "transform",
                    }},]
                    
                }},
                
                {{
                    name: "BushFactory(1090821408).spawn_placeholder(1)",
                    type:"Xform",
                    variables: "transform", 
                    children: [{{
                        name: "Tree.007",
                        type: "Xform",
                        variable: "transform",
                    }},]
                }},
                
                {{
                    name: "CameraRigs/0/0",
                    type: "Xform",
                    variables: "transform", 
                    children: [{{
                        name:"Camera.001",
                        type: "Camera",
                        variable: "clippingRange", "focalLength","horizontalAperture","horizontalApertureOffset","projection","verticalAperture","verticalApertureOffset"
                    }},]
                }},
                
                {{
                    name:"animhelper.SnakeFactory(1090821408).create_placeholder(0).p",
                    type: "Xform",
                    variables: "transform",
                    children: [
                        {{
                            name:"animhelper.SnakeFactory(1090821408).create_placeholder(0).p",
                            type: "BasisCurves",
                            variables: "curveVertexCounts","points","token_type","widths","token wrap"
                        }},
                        {{
                            name:"animhelper.SnakeFactory(1090821408).create_placeholder(0).path",
                            type: "Xform",
                            variables: "transform",
                            children: [
                                {{
                                    name: "policy_path_curve",
                                    type: "NurbsCurves",
                                    variables:"curveVertexCounts.timeSamples","knots.timeSamples","order.timeSamples","points.timeSamples","widths","widths.timeSamples",
                                }}
                            ]
                        }},
                    ]
                }},

                {{
                    name: "Empty",
                    type: "Xform",
                    variables: "transform",
                }},

                {{
                    name: "OpaqueTerrain_unapplied",
                    type: "Xform",
                    variables: "transform",
                }}
            ]
    
    """  

    """
    {{
                        name: "BushFactory(1090821408).spawn_placeholder(0)",
                        loc: (-18.240537643432617, 12.547088623046875, -0.21547305583953857),
                        rot: ((-0.6025745272636414, 0.7980626225471497, 0, 0), (-0.7980626225471497, -0.6025745272636414, 0, 0), (0, 0, 1, 0))
                    }},
                    {{
                        name: "Tree_006",
                        transform: ((1, 0, 0, 0), (0, 1, 0, 0), (0, -0, 1, 0), (0, 0, 0, 1))
                    }},
                    {{
                        name: "BushFactory(1090821408).spawn_placeholder(1)",
                        loc: (-68.22119140625, -60.60371780395508, 0.5133972764015198),
                        rot: ((-0.5922908782958984, 0.8057242035865784, 0, 0), (-0.8057242035865784, -0.5922908782958984, 0, 0), (0, 0, 1, 0))
                    }},
                    {{
                        name: "Tree_007",
                        tra
    """


    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_prompt),
            ("human", "{context}"),
        ]
    )

    # question_answer_chain = create_stuff_documents_chain(model, qa_prompt)
    question_answer_chain = qa_prompt | model | StrOutputParser()
    # rag_chain = create_retrieval_chain(embedder.retriever, question_answer_chain)
    embedder.load_db()
 
    new_db = []
    count = 0
    for seg in tqdm(embedder.texts):
        prompt = seg.page_content
        prompt = prompt.replace("{", "{{")
        prompt = prompt.replace("}", "}}")
        # print("prompt:",prompt)
        # print("##########################\n")/
        answer = question_answer_chain.invoke({"context": prompt})
        # print("answer:",answer)
        # print("##########################\n")
        new_db.append(Document(page_content=answer,metadata={'doc_id':f'id_{count}'}))
        count += 1
        # if count == 5:
        #     break
   
    # # Save the variable to a pickle file
    with open("all_new_db.pkl", "wb") as file:
        pickle.dump(new_db, file)
    #load from pickle file
    # print("loading from pickle:")
    # with open("all_new_db.pkl", 'rb') as file:
    #     new_db = pickle.load(file)
    print("finish loading all_new_db")
    #add doc id for each doc:
    db_with_metadata = []
    count = 0
    for d in new_db:
        content = d.page_content
        db_with_metadata.append(Document(page_content=content,metadata={'doc_id':f'id_{count}'}))
        count += 1




    ###update here to change the embedding to per function  setting. 


    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    condense_texts = text_splitter.split_documents(db_with_metadata)
    # print("Condensed text length is:",condense_texts)
    # condense_db = FAISS.from_documents(condense_texts, embedding= embedder.hf)
    db2 = Chroma.from_documents(condense_texts, embedder.hf, persist_directory="./fixed_chroma_db_desert_snake")

    # print("Saved chroma concise_faiss_index")
    #create vector store space for name only db
    name_db = Chroma(collection_name="full_documents", embedding_function=embedder.hf,persist_directory="./fixed_chroma_name_db_desert_snake")

    #extract the content after name and before type:
    pattern = r'name[\"]?\s*\:\s*["\'](.*?)["\'].*?[\n,]?\s*[\"]?type'
    name_doc = []
    doc_ids = []
    for doc in condense_texts:
        # print("doc is:",doc)
        match = re.search(pattern, doc.page_content)
        if not match:
            print("NOt matching:",doc)
        extracted_name = match.group(1)
        name_doc.append(Document(page_content=extracted_name, metadata={'doc_id': doc.metadata['doc_id']}))
        doc_ids.append(doc.metadata['doc_id'])
        # if 'snake' in extracted_name.lower():
        #     print(doc)
        # print("Check metadata:")
        # print(doc['metadata']['id_key'])
        
    
    # The storage layer for the parent documents
    store = InMemoryByteStore()
    id_key = "doc_id"

    # The retriever (empty to start)
    retriever = MultiVectorRetriever(
        vectorstore=name_db,
        byte_store=store,
        id_key=id_key,
    )

    retriever.vectorstore.add_documents(name_doc)
    retriever.docstore.mset(list(zip(doc_ids, condense_texts)))
    with open('name_retriever_store.pkl', 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(retriever.byte_store.store, outp, pickle.HIGHEST_PROTOCOL)

    print("Saved name retriever to local")
    # docsearch = FAISS.load_local("faiss_index", embeddings) 
    # while True:
        

    print("Testing...\n")
    prompt = "make the camera follow the snake for 10 sec and then stop moving"


    print(retriever.vectorstore.similarity_search_with_relevance_scores(
        query=prompt,
        k=len(doc_ids),
    # filter=[{"term":{"metadata.source.keyword":"news"}}],
    ))
    # print(retriever.vectorstore.similarity_search(prompt)[0])

    print(retriever.invoke(prompt)[0].page_content)
      
        
    #     prompt = input("Question: ")    #"write an infinigen command that will create an under water scene with snake in it."#


    #     answer = rag_chain.invoke({"input": prompt, "chat_history": chat_history})
        
    #     chat_history.extend([HumanMessage(content=prompt), AIMessage(content=answer['answer'])])
       
       

if __name__ == "__main__":
    main()
