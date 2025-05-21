from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

chat_model=AzureChatOpenAI(
    azure_endpoint=azure_openai_endpoint,
    openai_api_version=azure_openai_api_version,
    azure_deployment=azure_openai_deployment,
    model_name="gpt-4",

)
prompt=PromptTemplate(
    template='Write a summary for the following Poem - \n{poem}',
    input_variables=['poem']
)
parser=StrOutputParser()

## text loader is a simple text file loader
'''
TextLoader is a simple and commonly used document loader in LangChain that reads plain text (.txt) files and converts them into LangChain Document objects.
Use Case
• Ideal for loading chat logs, scraped text, transcripts, code snippets, or any plain text data into a LangChain pipeline.
Limitation
• Works only with txt files'''
from langchain_community.document_loaders import TextLoader
loader= TextLoader('cricket.txt',encoding='utf-8')
docs= loader.load()
# print(type(docs))
# print(len(docs))
# print(docs[0])
# print(docs[0].page_content)
# print(docs[0].metadata)

chain=prompt | chat_model | parser
result=chain.invoke({'poem':docs[0].page_content})
print(result)