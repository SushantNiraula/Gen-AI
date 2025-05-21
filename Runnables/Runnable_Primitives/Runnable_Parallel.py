from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel,RunnableSequence
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

## importing the environment variables
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

model=AzureChatOpenAI(
    azure_endpoint=azure_openai_endpoint,
    openai_api_version=azure_openai_api_version,
    azure_deployment=azure_openai_deployment,
    model_name="gpt-4",
)

prompt1= PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Generate a LinkedIn post about {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'LinkedIn post': RunnableSequence(prompt2,model,parser)
}
)
print(parallel_chain.invoke({"topic":"AI"}))