## Structured Output Parser is used to enforce schema and structure in the output of the model.
## But no data validation.
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser
from langchain.output_parsers import ResponseSchema


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
schema= [
    ResponseSchema(name='fact_1',description='first fact about the topic'),
    ResponseSchema(name='fact_2',description='second fact about the topic'),
    ResponseSchema(name='fact_3',description='third fact about the topic'),
    ResponseSchema(name='fact_4',description='fourth fact about the topic'),
    ResponseSchema(name='fact_5',description='fifth fact about the topic'),
]
parser=StructuredOutputParser.from_response_schemas(schema)
template1= PromptTemplate(
    template='Give 5 facts about the topic {topic}\n{format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions() }
)
prompt=template1.invoke({'topic':'Black Hole'})
result=chat_model.invoke(prompt)
final_result=parser.parse(result.content)
print(final_result)
