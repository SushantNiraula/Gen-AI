## to run virtual environment use source ./venv/bin/activate
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm= OpenAI(model='gpt-3.5-turbo-instruct')

result=llm.invoke("What is the capital of France?") # this will return a string

print(result)