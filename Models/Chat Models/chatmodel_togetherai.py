from langchain_together import ChatTogether
import dotenv

dotenv.load_dotenv()

chat_model= ChatTogether(
    model='meta-llama/Llama-3.3-70B-Instruct-Turbo-Free'
)

result=chat_model.invoke("What is the capital of France?")
print(result.content)