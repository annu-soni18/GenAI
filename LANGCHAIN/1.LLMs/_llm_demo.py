from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3",
    temperature=0.5
)

prompt = "what is capital of India in one sentence"

response = llm.invoke(prompt)
print(response.content)