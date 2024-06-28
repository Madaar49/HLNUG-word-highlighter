import streamlit as st


def app():
    st.header("Welcome to the PDF Highlighter App!")

    st.image("img/highlighter.jpg", caption="Highlight your PDFs effortlessly", use_column_width=True)

    st.markdown("""
    #### Highlight Your PDFs Effortlessly

    #### Get Started
    - Navigate to the "Single PDF Highlighter" or "Multiple PDFs Highlighter" pages using the menu on the left.
    - If you need instructions about how to use, please navigate to the **About** page
                
    """)


    st.write("© 2024 HLNUG. All rights reserved.")
