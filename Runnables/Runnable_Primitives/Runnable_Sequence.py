from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

chat_model=AzureChatOpenAI(
    azure_endpoint=azure_openai_endpoint,
    openai_api_version=azure_openai_api_version,
    azure_deployment=azure_openai_deployment,
    model_name="gpt-4",

)
prompt1= PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Write an explaination of the joke  {text}',
    input_variables=['text']
)
parser=StrOutputParser()
chain= RunnableSequence(prompt1, chat_model, parser, prompt2, chat_model, parser)
result=chain.invoke({'topic':'cricket'})
print(result)