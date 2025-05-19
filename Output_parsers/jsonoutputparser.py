from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

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
parser=JsonOutputParser()
template1= PromptTemplate(
    template='Give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions() }
)
# prompt= template1.format()
# # print(prompt) output is ::---> Return a JSON object. will be passed as prompt to the model
# result=chat_model.invoke(prompt)
# final_result=parser.parse(result.content)
# print(final_result)

## better way to do this to use chains
chain= template1 | chat_model | parser
result=chain.invoke({})
print(result)