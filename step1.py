import streamlit as st
from dotenv import load_dotenv

def main():
	load_dotenv()
	st.set_page_config(page_title="Chat con multiples PDFs", page_icon=":books:")


if __name__ == '__main__':
    main()
