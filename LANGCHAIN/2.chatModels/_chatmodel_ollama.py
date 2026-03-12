from langchain_ollama import ChatOllama

model = ChatOllama(model='llama3', temperature=1.5, max_completion_tokens=0)
result = model.invoke("give me best summer destination place")
print(result.content)