from dummy_LLM import DummyLLM
from dummy_PromptTemplate import DummyPromptTemplate

template=DummyPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length','topic']
)
prompt=template.format({'length':'short','topic':'Nepal'})
llm=DummyLLM()
print(llm.__predict__(prompt))
