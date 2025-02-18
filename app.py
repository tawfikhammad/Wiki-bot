import streamlit as st
from controller import Controller

st.title("Wikipedia QA Bot")

title = st.text_input("Enter the Wikipedia title to scrape:")
lang = st.selectbox("Select language", ["en", "ar"])

if title:
    if not title.strip():
        st.error("Please enter a valid title.")
    else:
        try:
            Cont = Controller(title, lang=lang)
            
            question = st.text_input("Ask a question:")
            if question:
                if not question.strip():
                    st.error("Please enter a valid question.")
                else:
                    # Get answer
                    answer = Cont.get_answer(question)
                    st.write("Answer:")
                    st.write(answer)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")