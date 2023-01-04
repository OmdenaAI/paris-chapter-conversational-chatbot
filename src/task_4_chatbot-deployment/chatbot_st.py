# -*- coding: utf-8 -*-
"""
@author: Pravitha
"""

import openai
import streamlit as st
#import streamlit_chat
from streamlit_chat import message
import json

openai.api_key = "API Key"

# Background image

img=Image.open("img1.jfif")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: cover;
background-position: left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


df=json.load(open('model_data.json','rb'))


def generate_reply(df):
    completions = openai.Completion.create(
    engine ="text-davinci-003",
    prompt=df,
    max_tokens=150,
    n=1,
    stop=None,
    temperature=0.7
    )
    
    message=completions.choices[0].text
    return message
  
#storing for chat
if "history" not in st.session_state:
    st.session_state.history = []

st.title("Omdena-Paris")
st.header("Conversational AI Chatbot for Elderly and Disabled")
st.subheader("GPT-3's 'text-davinci-003 model'")

def get_text():
    input_text=st.text_input("TALK TO THE BOT", key="input_text")
    return input_text

user_input =get_text()
if user_input:
    output=generate_reply(user_input)
    #store the output
    st.session_state.history.append({"message": user_input, "is_user": True })
    st.session_state.history.append({"message": output, "is_user": False})

    
for chat in st.session_state.history:
    message(**chat)  # unpacking
