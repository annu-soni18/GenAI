from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


model = ChatOllama(model = 'llama3')

# 1st prompt -> detailed prompt
template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template ='write a 5 line summary on the following text. /n {text}',
    input_variables = ['text']
)

prompt1 = template1.invoke({'topic': 'black hole'})
result1 = model.invoke(prompt1)
prompt2 = template2.invoke({'text':result1.content})
result2 = model.invoke(prompt2)
print(result2.content)