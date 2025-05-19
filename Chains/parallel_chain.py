from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

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
prompt1=PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)
prompt2=PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)
prompt3= PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n {notes} \n and {quiz}',
    input_variables=['notes','quiz']
)
parser=StrOutputParser()
## Create a chain that combines the prompt, model, and parser
parallel_chain=RunnableParallel(
    {
        'notes': prompt1 | model | parser,
        'quiz': prompt2 | model | parser
    }
)
## Create a chain that combines the prompt, model, and parser
chain= parallel_chain | prompt3 | model | parser
## Invoke the chain with a specific topic
text='''A Support Vector Machine (SVM) is a supervised machine learning algorithm used for both classification and regression tasks. It finds the optimal hyperplane that separates data points of different classes, maximizing the margin between them. SVMs can also handle non-linear data by mapping it to higher dimensions using kernels. 
Key aspects of SVMs: 
Supervised learning:
SVMs learn from labeled data to predict outcomes for new data. 
Classification and regression:
SVMs can be used to classify data into different categories or predict continuous values. 
Hyperplane:
SVMs find a hyperplane (a line in 2D, a plane in 3D, or a hyperplane in higher dimensions) that best separates data points of different classes. 
Margin:
The margin is the distance between the hyperplane and the nearest data points from each class. 
Support vectors:
The data points closest to the hyperplane are called support vectors, and they are crucial in determining the decision boundary. 
Kernels:
SVMs use kernel functions to map data to higher-dimensional spaces, allowing them to handle non-linear data. 
Effective in high-dimensional spaces:
SVMs perform well even when the number of features is greater than the number of samples. 
Resistant to overfitting:
SVMs tend to generalize well to new data because they focus on the margin, which helps to avoid over-fitting to the training data. 
Applications of SVMs: 
Image classification: SVMs can be used to classify images based on their features. 
Text classification: SVMs can be used to classify text documents based on their content. 
Handwriting recognition: SVMs can be used to recognize handwritten characters. 
Face detection: SVMs can be used to detect faces in images. 
Gene classification: SVMs can be used to classify genes based on their expression patterns. 
Web page classification: SVMs can be used to classify web pages based on their content. 
In essence, SVMs are a powerful tool for supervised learning, particularly for classification tasks, and they excel in situations with high-dimensional data or when dealing with complex non-linear relationship'''
result=chain.invoke({'text':text})
print(result)
## let's visualize the chain graph
chain.get_graph().print_ascii()