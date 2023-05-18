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
os.environ['PINECONE_API_KEY'] = '9a93d55a-836d-48f2-8aef-d327bf14d5d1'
os.environ['PINECONE_API_ENV'] = 'us-west1-gcp-free'
os.environ['PINECONE_INDEX'] = 'pdi'

# Enter your API key from Openai. 
# Link to keys: https://platform.openai.com/account/billing/overview
os.environ['OPENAI_API_KEY'] = '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'


# connect to Pinecone index = pdi, namespace = cd_8
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
pinecone = Pinecone.from_existing_index(index_name, embeddings, namespace='ce_8')
openAI = OpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])
chain = load_qa_chain(openAI, chain_type="stuff")


def askGPT(prompt):
    docs = pinecone.similarity_search(prompt)
    ch = chain.run(input_documents=docs, question=prompt)
    print(ch)

def main():
    while True:
        print('OpenAI + Pinecone: PDI CE 8\n')
        prompt = "prompt:" + input()
        
        askGPT(prompt)
        print('\n')
main()
