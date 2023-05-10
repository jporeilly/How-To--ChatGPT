## Chatbot for Financial Report 2016
# pip install langchain
# pip install openai
# pip install pinecone-client
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
import os
import pinecone

# Enter your API key & region from Pinecone. 
# Link to keys: https://platform.openai.com/account/billing/overview
PINECONE_API_KEY = 'fd59ad27-4abe-4292-a743-7ef93e4d860e'
PINECONE_API_ENV = 'us-west1-gcp-free'

# Enter your API key from Openai. 
# Link to keys: https://platform.openai.com/account/billing/overview
os.environ['OPENAI_API_KEY'] = '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'

# connect to Pinecone index = financial, namespace = FR_2016
pinecone.init(
    api_key=PINECONE_API_KEY,  
    environment=PINECONE_API_ENV
)
index_name = 'financial' 

# create embeddings using OpenAI. Temperature = 0 to stop waffle
embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])
pinecone = Pinecone.from_existing_index(index_name, embeddings)
openAI = OpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])
chain = load_qa_chain(openAI, chain_type="stuff")


def askGPT(prompt):
    docs = pinecone.similarity_search(prompt, include_metadata=True)
    ch = chain.run(input_documents=docs, question=prompt)
    print(ch)

def main():
    while True:
        print('OpenAI + Pinecone: Financial Report 2016\n')
        prompt = "prompt:" + input()
        
        askGPT(prompt)
        print('\n')
main()
