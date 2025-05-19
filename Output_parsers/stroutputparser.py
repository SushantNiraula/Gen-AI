from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

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
template1= PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic'],
)
template2=PromptTemplate(
    template='Write a 5 line summary on the following text: {text}',
    input_variables=['text'],
)
parser=StrOutputParser()
chain = template1 | chat_model | parser | template2 | chat_model | parser  ## Here we are using the StrOutputParser to parse the output of the first prompt and use it as input to the second prompt.
result= chain.invoke({'topic':'Black Hole'})
print(result)
## much easier and cleaner approach to chaining prompts and parsing outputs.

