## This chatbot will be working on our console.
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
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
chat_history =[
    SystemMessage(content='You are a helpful assistant.'),
]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower()=='exit':
        break
    response=chat_model.invoke(chat_history)
    chat_history.append(AIMessage(response.content))
    print(f"Chatbot: {response.content}")
# ## This chatbot will be working on our console.
'''
You: What is the capital of Nepal?
Chatbot: The capital of Nepal is Kathmandu.
You: Which one is greater 2 or 0.
Chatbot: 2 is greater than 0.
You: Now multiply the bigger number by 10.
Chatbot: The bigger number is 125. 
When multiplied by 10, the result is 1250.
 
        Problem here is that the chatbot is not able to understand the context of the previous question.
        It is not able to understand that the bigger number is 2 and not 125.'''
## even we got chat history, but there are problems i.e we kept all the user and ai response directly in the chat history with out 
## telling which message is from user and which one is from ai.