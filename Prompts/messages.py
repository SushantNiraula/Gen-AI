from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()
model= AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    model_name="gpt-4",
    max_tokens=400
)
messages=[
    SystemMessage(content='You are a helpful assistant.'),
    HumanMessage(content='explain the difference between static and dynamic prompts in the context of LLMs'),
]

response=model.invoke(messages)
messages.append(AIMessage(response.content))


print(messages)
print(response.AIMessage.content)