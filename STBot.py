import streamlit as st
from chatbot import ChatBot
from knowledgebase import KnowledgeBase
from feedbackprocessor import FeedbackProcessor

def initialize_chatbot():
    kb = KnowledgeBase()
    feedback_processor = FeedbackProcessor(kb)
    chatbot = ChatBot(feedback_processor, kb)
    return chatbot

def main():
    st.set_page_config(page_title="Senffinho Chatbot", page_icon=":robot_face:")
    st.title("Senffinho Chatbot")

    chatbot = initialize_chatbot()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Digite sua pergunta aqui..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = chatbot.get_response(st.session_state.messages)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()