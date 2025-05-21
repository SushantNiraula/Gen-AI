## Runnable Passthrough
# This runnable does not modify the input data and simply passes it through.
# It is useful for debugging or when you want to create a chain of runnables
# where some of them do not modify the data.
from langchain.schema.runnable import RunnablePassthrough,RunnableSequence,RunnableParallel
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
    'explaination':RunnableSequence(prompt2, model, parser)
}
)

final_chain=RunnableSequence(
    joke_gen_chain,
    parallel_chain

)
result=final_chain.invoke({'topic':'cricket'})
print(result['joke'])
print(result['explaination'])
