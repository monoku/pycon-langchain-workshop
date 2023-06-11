import streamlit as st
from dotenv import load_dotenv
from htmlcss import bot_template, user_template, css
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.indexes import VectorstoreIndexCreator


def get_youtube_transcription(youtube_url):
    from langchain.document_loaders import YoutubeLoader
    loader = YoutubeLoader.from_youtube_url(youtube_url, add_video_info=True, language=['en','es'])
    return loader.load()


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat con un video de YouTube", page_icon="📹")
    st.write(css, unsafe_allow_html=True)
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    st.header("Chat con con un video de YouTube 📹")
    user_question = st.text_input("Pregúntale lo que quieras al video:")
    if user_question:
        handle_userinput(user_question)
    with st.sidebar:
        st.subheader("Tu video a consultar")
        youtube_url = st.text_input("Agrega la URL del video de YouTube aquí")
        if youtube_url:
            with st.spinner("Procesando..."):
                youtube_transcription = get_youtube_transcription(youtube_url)
                index = VectorstoreIndexCreator().from_documents(youtube_transcription)
                st.session_state.conversation = get_conversation_chain(index.vectorstore)

if __name__ == '__main__':
    main()
