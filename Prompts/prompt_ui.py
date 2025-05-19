from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
import os
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
chat_model=AzureChatOpenAI(
    azure_endpoint=azure_openai_endpoint,
    openai_api_version=azure_openai_api_version,
    azure_deployment=azure_openai_deployment,
    model_name="gpt-4",
)
st.header("Research Tool")
user_input=st.text_input("Enter your research question:")
if st.button('Submit'):
    response=chat_model.invoke(user_input)
    st.write(response.content)

