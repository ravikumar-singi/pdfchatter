import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

def main():
    st.set_page_config(page_title="Chat with multiple PDFs",page_icon=":books:")

    st.header("Chat with multiple PDFs :books:")
    st.text_input("ask a question about your documents:")

    with st.sidebar:
        st.subheader("your documents")
        pdf_docs = st.file_uploader("upload your PDFs here and Click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                #get pdf text
                raw_tet= get_pdf_text(pdf_docs)
                #st.write(raw_text)
                # get text chunk
                # create vector store

if __name__=='__main__':
    main()