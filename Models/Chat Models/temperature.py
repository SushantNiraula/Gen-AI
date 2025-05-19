from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

chat_model= AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    azure_deployment=azure_deployment_name,
    openai_api_version=azure_api_version,
    temperature=0,
    model_name="gpt-4",
    max_tokens=100,
)

result=chat_model.invoke("Write a 5 line poem about cricket")
print(result.content)

