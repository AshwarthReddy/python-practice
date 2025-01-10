import streamlit as st;
import os;
import google.generativeai as genai

st.title('Prompt Engineering Example')

genai.configure(api_key="API_KEY")

user_input = st.text_input('Enter Your Query')


model = genai.GenerativeModel("gemini-1.5-flash")



if st.button('Submit'):
    response = model.generate_content(user_input)
    response.text
    st.write(response.text)



# streamlit run app.py