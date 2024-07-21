import streamlit as st

def app():
    st.title("About PDF Highlighter App")

    st.markdown("""
    ## Dear User, 
    ### Welcome to the PDF Highlighter App!

    This application is designed to help you easily highlight words in PDF documents. It is efficient in highlighting a single word or multiple word, in a single PDF or multiple PDFs in a batch process.

    ### Features
    - **Single PDF Highlighter**:
        - Highlight a specific word in a single PDF document with user defined colors
        - Highlight multiple  words in a single PDF document with different user defined colors
    - **Multiple PDFs Highlighter**: Batch process multiple PDF documents in a folder.
        - Highlight single or multiple  words multiple PDF document in a folder, with user defined colors
    - **Customizable Colors**: Choose different colors for different words to differentiate  your highlighted text.
    - **User-Friendly Interface**: Easy-to-use interface powered by Streamlit, making the process simple and fast.

    ### How It Works
    #### Single PDF
    - **Upload a PDF**: Upload a single PDF by drag & drop, or browse to the directory.
    - **Specify Words and Colors**: 
        - After uploading a PDF, use the "+" sign at the corner of the box to choose how many unique words you want to highlight 
        - Select the corresponding colors under each word
    - **Download Highlighted PDFs**: After processing, download the highlighted PDF documents directly from the app.
    - ** Output**: 
                - A summary statistics of the frequency of highlighted words in the PDF
                - Highlighted PDFs based on word and color match.
                
    #### Multiple PDF 
    - **Upload the Folder path**: For multiple PDFs, copy and paste the path of your folder.
                - Select number of unique words and corresponding colors.
                - specify the input folder and the app will process all PDFs in that folder, saving the highlighted versions to an output folder.
    - **Download Highlighted PDFs**: After processing, download the highlighted PDF documents directly from the app.
    - **Output Location**: After processing, the highlighted PDFs will be located in an "output folder", located in your input folder.
    - ** Output**: For every PDF
                - A summary statistics of the frequency of highlighted
                - Highlighted PDF based on word and color match.
                
    ### Technologies Used
    - **Streamlit**: For creating the web application interface.
    - **PyMuPDF (Fitz)**: For reading and manipulating the PDF files.
    - **Python**: The core programming language used to develop the application.

    ### Support
    This app was designed courtsey of HLNUG, Wiesbaden. In case of any technical problems with the app, please reach out to "Augustine-Maada.Gbondo@hlnug.hessen.de".
    Hope you find this tool useful and easy to use. Feedback and suggestions are always welcome.

    """)
