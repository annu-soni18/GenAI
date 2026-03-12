from langchain_ollama import ChatOllama
import streamlit as st

from langchain_core.prompts import load_prompt, PromptTemplate

llm = ChatOllama(
  model="llama3"
)

st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need",
"BERT: pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-shot Learners", 
"Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", 
 "Mathematical"   ])

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraph)", "Long (detailed explanation)"])


# template
template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | llm
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)