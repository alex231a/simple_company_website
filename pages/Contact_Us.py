import streamlit as st
from send_email import send_email
import pandas as pd

list_m = []
df = pd.read_csv('topics.csv')

st.header("Contact Me")

with st.form(key='email'):
    email_adress = st.text_input("Your email adress")
    topic = st.selectbox('What topic would you like to discuss?', (df['topic']))
    message = st.text_area("Your message")
    message = message + "\n" + email_adress
    button = st.form_submit_button("Submit")
    if button:
        send_email(message, topic)
        st.info("email was sent successfully")
