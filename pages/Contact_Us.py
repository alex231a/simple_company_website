import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key='email'):
    email_adress = st.text_input("Your email adress")
    message = st.text_area("Your message")
    message = message + "\n" + email_adress
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("email was sent successfully")
