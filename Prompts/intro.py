## Prompts are the input instructions or queries given to the model to guide its output.

## Static prompts are fixed and do not change.
## Dynamic prompts are generated based on the context or previous interactions.
from langchain_openai import AzureChatOpenAI
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
response=chat_model.invoke('explain the difference between static and dynamic prompts in the context of LLMs')
print(response.content)