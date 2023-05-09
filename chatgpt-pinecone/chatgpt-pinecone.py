# Chatbot for Financial Report
# pip install langchain
import pinecone
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
import os

# connect to Pinecone index financial
pinecone.init(
    api_key='PINE API KEY',  
    environment='PINECONE REGION'  
)
index_name = "financial"

# create embeddings using OpenAI. Temperature = 0 to stop waffle
embeddings = OpenAIEmbeddings(openai_api_key='')
pinecone = Pinecone.from_existing_index(index_name,embeddings)
openAI = OpenAI(temperature=0, openai_api_key='')
chain = load_qa_chain(openAI, chain_type="stuff")


def askGPT(prompt):
    docs = pinecone.similarity_search(prompt, include_metadata=True)
    ch = chain.run(input_documents=docs, question=prompt)
    print(ch)

def main():
    while True:
        print('Open AI + Pinecone: Financial Report 2016\n')
        prompt = "prompt:" + input()
        
        askGPT(prompt)
        print('\n')
main()
