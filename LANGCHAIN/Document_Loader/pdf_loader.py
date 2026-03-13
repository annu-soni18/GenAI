from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"D:\GenAI\LANGCHAIN\Document_Loader\Attention (Research Paper).pdf")
documents = loader.load()
print(len(documents))
print(documents[0].page_content)
print(documents[0].metadata)