from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
## create chat prompt template
chat_template= ChatPromptTemplate([
    ('system','You are a helpful Customer Support Agent.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
    
])

chat_history=[]
with open('chat_history.txt','r') as f:
    chat_history.extend(f.readlines())

user_query=input('Enter your query:')
prompt=chat_template.invoke({'chat_history':chat_history, 'query':user_query})
with open('chat_history.txt','a') as f:
    f.write(f'{user_query}\n')

print(prompt)
