import streamlit as st
import fitz 
import os


color_options = {
    "Red": (1, 0, 0),
    "Green": (0, 1, 0),
    "Blue": (0, 0, 1),
    "Yellow": (1, 1, 0),
    "Cyan": (0, 1, 1),
    "Magenta": (1, 0, 1),
    "Black": (0, 0, 0),
    "White": (1, 1, 1)
    }


def highlight_words(pdf_path, color_type):
    doc = fitz.open(pdf_path)
    for page in doc:
        for word, color in color_type.items():
            text_instances = page.search_for(word)
            for inst in text_instances:
                highlight = page.add_highlight_annot(inst)
                highlight.set_colors(stroke=color)
                highlight.update()
    highlighted_pdf_path = "highlighted_" + os.path.basename(pdf_path)
    doc.save(highlighted_pdf_path)
    return highlighted_pdf_path

# Streamlit app
def app():

    st.title("Single PDF Highlighter")
    uploaded_file = st.file_uploader("Upload a PDF file",
                                    type=["pdf"])
    if uploaded_file:
        st.write("Uploaded file:",
                uploaded_file.name)
        color_type = {}
        num_words = st.number_input("Number of words to highlight",
                                    min_value=1, step=1)
        for i in range(num_words):
            word = st.text_input(f"Word {i+1}")
            color_name = st.selectbox(f"Pick a color for word {i+1}",
                                    list(color_options.keys()))
            if word and color_name:
                color_type[word] = color_options[color_name]
        
        if st.button("Highlight Words"):
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            highlighted_pdf_path = highlight_words(uploaded_file.name,
                                                    color_type)
            st.write("Highlighted PDF saved as:",
                    highlighted_pdf_path)
            with open(highlighted_pdf_path, "rb") as file:
                btn = st.download_button(
                    label="Download Highlighted PDF",
                    data=file,
                    file_name=highlighted_pdf_path,
                    mime="application/pdf"
                    )