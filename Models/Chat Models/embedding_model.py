from langchain.embeddings import HuggingFaceEmbeddings

import dotenv
dotenv.load_dotenv()
embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents=[
    'kathmandu is the capital of nepal.',
    'china has the capital of beijing.',
    'india has the capital of new delhi.',
]
text="Kathmandu is the capital of Nepal."

embedding_vector=embedding.embed_query(documents[0])
print(str(embedding_vector))