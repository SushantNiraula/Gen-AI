##SequentialChain: A chain that executes multiple steps sequentially, passing results between them.
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

## from environment variables import the azure openai endpoint, api version, deployment name and model name
load_dotenv()
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
azure_open_ai_model = os.getenv("AZURE_OPENAI_MODEL_NAME")
## Initialize the AzureChatOpenAI model
model=AzureChatOpenAI(
    azure_endpoint=azure_openai_endpoint,
    openai_api_version=azure_openai_api_version,
    azure_deployment=azure_openai_deployment,
    model_name=azure_open_ai_model,
)
template_report= PromptTemplate(
    template='Generate a detailed report on {topic} \n',
    input_variables=['topic']

)
parser= StrOutputParser()
template_summary= PromptTemplate(
    template='Summarize the report on {topic} \n',
    input_variables=['topic']
)

## Create a chain that combines the prompt, model, and parser
chain =template_report | model | parser | template_summary | model | parser
## Invoke the chain with a specific topic
result=chain.invoke({'topic':'Python programming'})
print(result)

