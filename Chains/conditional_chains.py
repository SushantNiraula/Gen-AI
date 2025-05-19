## Conditional chains or RouterChain: Directs inputs to different chains based on conditions (useful for multi-task AI applications).

## we are building a conditional chain that can route inputs to different chains based on the input type.
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
## for output parser to get the output as positive or negative only
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()
## import the azure openai endpoint, api version, deployment name and model name from environment variables
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

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive','negative']= Field(description="The sentiment of the feedback text")

parser2= PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative: \n {text}\n {format_instruction}',
    input_variables=['text'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)


classifier_chain=prompt1 | model | parser2

# result=classifier_chain.invoke(
#     {
#         'text': 'The product is great and works perfectly!'
#     }
# ).sentiment
# print(result) ## we got output as Sentiment: **Positive**
# we got output as Sentiment: **Positive** 
## But we want to get the output as positive or negative only.
## so we will use the output parser to get the output as positive or negative only.
prompt2=PromptTemplate(
    template='Write an appropriate response to this positive feedback: \n {text}',
    input_variables=['text']
)
prompt3=PromptTemplate(
    template='Write an appropriate response to this negative feedback: \n {text}',
    input_variables=['text']
)


branch_chain= RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: 'Could not classify the sentiment of the feedback text')
)
chain=classifier_chain | branch_chain
## Invoke the chain with a specific topic
result=chain.invoke(
    {
        'text': 'The product is great and works perfectly!'
    }
)
print(result) ## we got output as Sentiment: **Positive**