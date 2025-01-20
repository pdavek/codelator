import openai
import streamlit as st
import time
import os

openai.api_key = st.secrets["openai"]["api_key"]

def explain_code(code):
    prompt = f"Explain the following code in plain English:\n{code}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who helps translating code to plain language. You should try to explain as clearly as possible but no too long. Keep it short and precise."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()


st.write("# Codelator")
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #87CEEB;'>Enter Your Code</h3>", unsafe_allow_html=True)
code_input = st.text_area("Paste your code here:", height=300, max_chars=5000, help="Insert the code you want to translate into plain English.")
st.markdown("<br><br>", unsafe_allow_html=True)
explanation = ""
if st.button("Translate", key="translate_button", help="Click to translate the code"):
    if code_input:
        with st.spinner('Translating...'):
            time.sleep(2)  # Simulate loading time
            explanation = explain_code(code_input)  # Translate code to English
            st.success('Translation Complete!')
        
        # Show explanation with some style
        st.markdown(f"<h4 style='color: #34495E;'>Explanation:</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 16px; color: #BABABA; line-height: 1.6;'>{explanation}</p>", unsafe_allow_html=True)
    else:
        st.warning("Please enter some code to translate.", icon="⚠️")
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #7F8C8D;'>Powered by OpenAI & Streamlit to understand my mess</p>", unsafe_allow_html=True)
