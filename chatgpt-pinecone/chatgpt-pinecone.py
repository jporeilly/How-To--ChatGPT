## Chatbot for PDI CE 8
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
os.environ['PINECONE_API_KEY'] = 'a8f51597-92c6-4f5a-bbf3-420052427b55'
os.environ['PINECONE_API_ENV'] = 'us-west1-gcp-free'
os.environ['PINECONE_INDEX'] = 'financial'

# Enter your API key from Openai. 
# Link to keys: https://platform.openai.com/account/billing/overview
os.environ['OPENAI_API_KEY'] = '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'


# connect to Pinecone index = financial, namespace = FR_2016
pinecone.init(
    api_key=os.environ['PINECONE_API_KEY'],  
    environment=os.environ['PINECONE_API_ENV']
)
# create an index - financial commented out for free tier
# pinecone.create_index(os.environ['PINECONE_INDEX'],
#                      dimension=1536,
#                      metric='cosine',
#                      metadata_config={
#                          "indexed": ['source', 'source_id', 'url', 'created_at', 'author', 'document_id']})

# create embeddings using OpenAI. Temperature = 0 to stop waffle
index_name = os.environ['PINECONE_INDEX']
embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])
pinecone = Pinecone.from_existing_index(index_name, embeddings, namespace='FR_2016')
openAI = OpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])
chain = load_qa_chain(openAI, chain_type="stuff")


def askGPT(prompt):
    docs = pinecone.similarity_search(prompt)
    ch = chain.run(input_documents=docs, question=prompt)
    print(ch)

def main():
    while True:
        print('OpenAI + Pinecone: Financial\n')
        prompt = "prompt:" + input()
        
        askGPT(prompt)
        print('\n')
main()
