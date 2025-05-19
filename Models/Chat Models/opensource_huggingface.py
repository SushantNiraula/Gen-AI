from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import dotenv
dotenv.load_dotenv()

# Initialize the HuggingFace model
llm= HuggingFaceEndpoint ( repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", task="text-generation")

model=ChatHuggingFace(llm=llm)

result=model.invoke("Whcat is the capital of France?")
print(result.content)