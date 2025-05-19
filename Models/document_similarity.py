from dotenv import load_dotenv
import os
load_dotenv()
from langchain_openai import AzureOpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

open_ai_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
open_ai_api_version=os.getenv("AZURE_OPENAI_API_VERSION")
open_ai_api_key=os.getenv("AZURE_OPENAI_API_KEY")
open_ai_deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=open_ai_endpoint,
    azure_deployment=open_ai_deployment_name,
    openai_api_version=open_ai_api_version,
    dimensions=500,
)
documents=[
    'Virat Kohli is an Indian cricketer and former captain of the Indian national team. He is widely regarded as one of the best batsmen in the world and has numerous records to his name.',
    'Sachin Tendulkar is a former Indian cricketer and captain of the Indian national team. He is often referred to as the "God of Cricket" and holds the record for the most runs in international cricket.',
    'Rohit Sharma is an Indian cricketer and the current captain of the Indian national team. He is known for his aggressive batting style and has scored multiple double centuries in One Day Internationals (ODIs).',
    'MS Dhoni is a former Indian cricketer and captain of the Indian national team. He is known for his calm demeanor and exceptional leadership skills, leading India to victory in the 2007 ICC T20 World Cup and the 2011 ICC Cricket World Cup.',
    'Kapil Dev is a former Indian cricketer and captain of the Indian national team. He is best known for leading India to its first Cricket World Cup victory in 1983 and is regarded as one of the greatest all-rounders in cricket history.',
    'Sunil Gavaskar is a former Indian cricketer and captain of the Indian national team. He is known for his exceptional batting skills and was the first player to score 10,000 runs in Test cricket.',
]

query= 'tell me about virat kohli'
# Get the embeddings for the documents
doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)
scores=cosine_similarity([query_embedding], doc_embeddings)[0]
index,score=(sorted(list(enumerate(scores)),key=lambda x: x[1])[-1])

print(f"Most similar document: {documents[index]}")
print(f"Similarity score: {score}")

## we have not stored the embeddings in a database, so we are not using any vector store here.
## we are using sklearn to calculate the cosine similarity between the query and the documents.