from langgraph.prebuilt import create_react_agent
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os

model=AzureChatOpenAI(
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
    azure_deployment=os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME'),
    api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
    model=os.getenv('AZURE_OPENAI_MODEL_NAME')
)

def get_weather(city:str)-> str:
    '''Get the weather for a given city'''
    return f"it's always sunny in {city}"

agent=create_react_agent(
    model=model,
    tools=[get_weather],
    prompt="You are a helpful assistant"
)

result=agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
print(result)