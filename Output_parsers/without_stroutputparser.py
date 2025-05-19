from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
import os

azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
azure_open_ai_model = os.getenv("AZURE_OPENAI_MODEL_NAME")

chat_model=AzureChatOpenAI(
    azure_endpoint=azure_openai_endpoint,
    openai_api_version=azure_openai_api_version,
    azure_deployment=azure_openai_deployment,
    model_name=azure_open_ai_model,

)
template1= PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic'],
)
template2=PromptTemplate(
    template='Write a 5 line summary on the following text: {text}',
    input_variables=['text'],
)

prompt1=template1.invoke({'topic':'Black Hole'})
result=chat_model.invoke(prompt1)
prompt2=template2.invoke({'text':result.content})
result2=chat_model.invoke(prompt2)
print(result2.content)
## In this approach we used .content to get the content of the result and then used it as input to the next prompt.