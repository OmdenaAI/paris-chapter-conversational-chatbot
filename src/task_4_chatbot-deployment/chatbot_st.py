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

st.title("Omdena Chatbot")

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
