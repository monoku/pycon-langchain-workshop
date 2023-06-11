import streamlit as st
from dotenv import load_dotenv
from htmlcss import bot_template, user_template, css

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat con multiples PDFs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
