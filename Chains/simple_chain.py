from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
# Load environment variables
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
azure_open_ai_model = os.getenv("AZURE_OPENAI_MODEL_NAME")
# Initialize the AzureChatOpenAI model
model=AzureChatOpenAI(
    azure_endpoint=azure_openai_endpoint,
    openai_api_version=azure_openai_api_version,
    azure_deployment=azure_openai_deployment,
    model_name=azure_open_ai_model,
)
prompt= PromptTemplate(
    template='Generate 5 interesting facts about {topic} \n',
    input_variables=['topic']

)
parser=StrOutputParser()
# Create a chain that combines the prompt, model, and parser
chain =prompt | model | parser
# Invoke the chain with a specific topic
result=chain.invoke({'topic':'Python programming'})
print(result)
# The output will be a string containing the generated facts about Python programming.\
chain.get_graph().print_ascii()
## we visualize the chain graph
## we should install grandalf to visualize the chain graph