import streamlit as st
from dotenv import load_dotenv
from htmlcss import bot_template, user_template, css

def main():
	load_dotenv()
	st.set_page_config(page_title="Chat con multiples PDFs", page_icon=":books:")
	st.write(css, unsafe_allow_html=True)

	if "conversation" not in st.session_state:
		st.session_state.conversation = None
	if "chat_history" not in st.session_state:
		st.session_state.chat_history = None

	st.header("Chat con multiples PDFs :books:")
	user_question = st.text_input("Pregúntale lo que quieras a tus documentos PDFs:")
	with st.sidebar:
		st.subheader("Tus documentos")
		pdf_docs = st.file_uploader("Sube tus PDFs aquí y haz click en 'Procesar'", accept_multiple_files=True)

if __name__ == '__main__':
    main()
