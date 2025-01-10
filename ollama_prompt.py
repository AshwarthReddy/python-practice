from ollama import chat
from ollama import ChatResponse
import streamlit as st;
import os;
from io import StringIO
import fitz

st.title('Ollama, What can I help with?')

user_input = st.text_input('Ask Ollama OpenAi')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    doc = fitz.open('your_file.pdf')
    for page_num in range(doc.page_count):
    page = doc.load_page(page_num)
    text = page.get_text("text")
    print(f"Page {page_num + 1} content:")
    print(text)

if st.button('Submit'):
    response: ChatResponse = chat(model='llama3.2:3b', messages=[
   {
    'role': 'user',
    'content': user_input,
  },
])
    st.write(response.message.content)




# streamlit run ollama_prompt.py