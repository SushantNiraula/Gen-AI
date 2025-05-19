from langchain_openai import AzureChatOpenAI
from typing import TypedDict, Annotated
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

class Review(TypedDict):
    summary:Annotated[str, "summary explaining the overall review with all the negative as well as positive part well emphasized"] ## Annotated typedict where we are using the Annotated type hint to add a description to the field
    sentiment:str ## simple typedict

structured_model=chat_model.with_structured_output(Review)
result=structured_model.invoke("The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI Joks outdated compared to other brands. Hoping for a software update to fix this.")
# result=chat_model.invoke("The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI Joks outdated compared to other brands. Hoping for a software update to fix this.")
# print(result.content)
print(result['summary'])
print(result['sentiment'])