import streamlit as st
import openai
from streamlit_lottie import st_lottie
import json
import time



import pickle 
from pathlib import Path

import streamlit_authenticator as stauth


st.set_page_config(page_title="Meu App Streamlit", page_icon=":tada:")    

#Page Authentification

names =["Matthias Maia ", "Helena Navis"]
usernames = ["matthias.maia", "helena.navis"]


file_path = Path(__file__).parent /"hashed_pw.pkl"
with file_path.open('rb') as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "students_resource", "abcdef", cookie_expiry_days=30)


name, authentication_status, password = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/Password incorrect")
if authentication_status == None:
    st.warning("Please, enter your username and password")
if authentication_status:    
    



    openai_api_key = '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'
    openai.api_key = openai_api_key


    def text_generator(words_list):
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um escritor de textos para estudantes de inglês."},
            {"role": "user", "content": f"Crie uma história em inglês para estudantes que tenha as palavras {words_list}. A história deve ter, no máximo, 150 palavras."},
            
        ]
    ) 
        return response.choices[0].message.content.strip('\"')


    def load_lottie_file(filepath: str):
        with open(filepath,'r') as f:
            return json.load(f)
    
    authenticator.logout("Logout", "sidebar")
    st.title('Gerador de Histórias')
    word_list=st.text_input("Quais palavras você quer revisar na sua história?")
    if word_list:
        my_placeholder = st.empty()
        my_message = st.empty()  
        with my_placeholder:
            st.write('Sua história está sendo escrita')
            time.sleep(3)

            st_lottie(load_lottie_file('animation_lnm49yam.json'), height=400,width=400)
            
        my_story = text_generator(word_list)
        my_placeholder.empty()
        st.write('Em seguida sua história:')
        time.sleep(3)
        st.write(my_story)








