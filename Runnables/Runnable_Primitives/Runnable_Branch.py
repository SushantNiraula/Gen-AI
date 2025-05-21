## Runnable_Branch is a runnable primitive that allows you to create conditional branches in your AI pipeline.
## It enables you to define different paths of execution based on the input data or the results of previous steps.
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Literal
import os
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()
from langchain.schema.runnable import RunnableSequence, RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

chat_model=AzureChatOpenAI(
    azure_endpoint=azure_openai_endpoint,
    openai_api_version=azure_openai_api_version,
    azure_deployment=azure_openai_deployment,
    model_name="gpt-4",

)
class SentimentAnalysis(BaseModel):
    sentiment: Literal['Payment','Delivery','Product','Service','Other']


prompt1= PromptTemplate(
    template='which type of query is being expressed by customer in the text {text}.',
    input_variables=['text']

)
prompt_Payment= PromptTemplate(
    template='Write a response to the customer for the Payment query {text}',
    input_variables=['text']

)
prompt_Delivery= PromptTemplate(
    template='Write a response to the customer for the Delivery query {text}',
    input_variables=['text']

)
prompt_Product= PromptTemplate(
    template='Write a response to the customer for the Product query {text}',
    input_variables=['text']

)
prompt_Service= PromptTemplate(
    template='Write a response to the customer for the Service query {text}',
    input_variables=['text']

)
parser=StrOutputParser()
sentiment_analysis_chain=prompt1 | chat_model.with_structured_output(SentimentAnalysis) 
payment_chain= prompt_Payment | chat_model | parser
delivery_chain= prompt_Delivery | chat_model | parser
product_chain= prompt_Product | chat_model | parser
service_chain= prompt_Service | chat_model | parser
response_chain=RunnableBranch(
    (lambda x: x=="sentiment='payment'" , payment_chain),
    (lambda x: x=="sentiment='delivery" , delivery_chain),
    (lambda x: x=="sentiment='product'" , product_chain),
    (lambda x: x=="sentiment='service'" , service_chain),
    (lambda x: x=="sentiment='other'" , chat_model),
    chat_model
)
final_chain = sentiment_analysis_chain | response_chain
## Run the chain
result=final_chain.invoke({"text":"I am not happy with the product I received. It is not working as expected."})
print(result)
