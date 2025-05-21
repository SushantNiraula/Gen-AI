## Runnable Lambda is a runnable primitive that allows you to apply custom Python functions within an AI Pipeline.

## It acts as a middleware between different AI components, enabling preprocessing, transformation , API calls, Filetering and postprocessing of data in Langchain Workflow.

from langchain.schema.runnable import RunnableLambda, RunnableSequence, RunnablePassthrough,   RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
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
    template='Make a joke about {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Write an explaination of the joke  {text}',
    input_variables=['text']
)
parser=StrOutputParser()
joke_gen_chain=RunnableSequence(prompt1, model, parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'count': RunnableLambda(lambda x: len(x.split()))
}
)
final_chain=RunnableSequence(
    joke_gen_chain,
    parallel_chain
)

## Run the chain
result=final_chain.invoke({"topic":"AI"})
print(result)