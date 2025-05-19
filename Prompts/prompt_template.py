from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os 
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")


chat_model=AzureChatOpenAI(
    azure_endpoint=azure_openai_endpoint,
    openai_api_version=azure_openai_api_version,
    azure_deployment=azure_openai_deployment,
    model_name="gpt-4",
)


# ## Prompt templates are a way to create dynamic prompts by filling in placeholders with specific values.
# ## They allow for more flexibility and customization in generating prompts.
st.header('Prompt Template')


paper_input=st.text_input("Enter the research paper title:")
style_input=st.selectbox("Select the explanation style:", ["Technical", "Layman"])
length_input=st.selectbox("Select the explanation length:", ["Short", "Medium", "Long"])

template= load_prompt('prompt_template.json')


if st.button('Summerize'):
    chain=template | chat_model
    result=chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    }
    
    ) 
    st.write(result.content)
