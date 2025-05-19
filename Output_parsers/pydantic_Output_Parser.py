from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv
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
class Person (BaseModel):
    name: str= Field(description='Name of the Person')
    age: int = Field(gt=18, description='Age of the Person')
    city: str = Field(description='City of the Person')

parser= PydanticOutputParser(pydantic_object= Person)

template=PromptTemplate(
    template= 'Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions() }
)

# prompt=template.invoke({'place':'Indian'})
# result=chat_model.invoke(prompt)
# final_result=parser.parse(result.content)
# print(final_result) 
# print(prompt)
chain= template | chat_model | parser
result=chain.invoke({'place':'Indian'})
print(result)