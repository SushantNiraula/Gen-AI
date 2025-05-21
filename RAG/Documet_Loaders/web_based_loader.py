from langchain_community.document_loaders import WebBaseLoader
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
loader=WebBaseLoader('https://www.amazon.com/Speech-Language-Processing-Daniel-Jurafsky/dp/0131873210?crid=3OFQAJDV0X9BA&dib=eyJ2IjoiMSJ9.NcPd0calpxQ8Q1AsQL5_v0SEiD9WG7yyKMuDWqvocvVL3LyzV3tLASgTWe_8v-Y0lJUlGJI22mHn9oqITTFerEt2ta0VAJUs4SKIi0SI5q3DZiOOzS_MqyqZvoZ5bbj7Ayuj1wSDGVF0mCo41EHtaiy9nT4Luwt5wZIDlbla4JMiS2bN7YlTjUquWtpBu5MJ2ChU5GaHAXAtsMENK8nD4As6c8CCRwiILgBKYDIbj6Y.fjit0ahlbv1zRp6NmFJgKSD2QePz0R-k50EV0mwBjr8&dib_tag=se&keywords=speech+and+language+processing&qid=1731366060&sprefix=speech+language+processing,aps,207&sr=8-1&linkCode=sl1&tag=thedatajourne-20&linkId=876047586dcea8d379ec74bde68dc80b&language=en_US&ref_=as_li_ss_tl')
data= loader.load()
parser=StrOutputParser()
prompt=PromptTemplate(
    template='Anser the following question {question} based on the following text - \n{text}'
    , input_variables=['question','text']
)
chain= prompt | chat_model | parser
result=chain.invoke({'question':'What is the book about?','text':data[0].page_content})
print(result)