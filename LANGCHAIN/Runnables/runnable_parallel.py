from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

model = ChatOllama(model="llama3")

prompt1 = PromptTemplate(
    template = "Generate a tweet about {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "Generate a LinkedIn post about {topic}",
    input_variables = ['topic']
)

parser = StrOutputParser()

chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'LinkedIn': RunnableSequence(prompt2,model,parser)
})

result = chain.invoke({'topic': 'LSTM'})
print(result)