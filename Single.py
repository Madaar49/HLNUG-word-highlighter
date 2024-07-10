import streamlit as st
import fitz  # PyMuPDF
import os
import tempfile
import io

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
    word_count = {}
    for page in doc:
        for word, color in color_type.items():
            text_instances = page.search_for(word)
            word_count[word] = word_count.get(word, 0) + len(text_instances)
            for inst in text_instances:
                highlight = page.add_highlight_annot(inst)
                highlight.set_colors(stroke=color)
                highlight.update()

    highlighted_pdf_path = "highlighted_" + os.path.basename(pdf_path)
    doc.save(highlighted_pdf_path)

# Create a summary PDF with word counts
    summary_doc = fitz.open()
    summary_page = summary_doc.new_page()
    summary_text = "Highlighted Words Statistics of document:\n\n"
    for word, count in word_count.items():
        summary_text += f"{word}: {count} occurrences\n"
    summary_page.insert_text((72, 72), summary_text, fontsize=14)
    
    # Save the summary PDF to an in-memory bytes buffer
    summary_pdf_buffer = io.BytesIO()
    summary_doc.save(summary_pdf_buffer)
    summary_pdf_buffer.seek(0)  # Rewind the buffer

    # Load the summary PDF from the buffer
    summary_doc = fitz.open("pdf", summary_pdf_buffer.read())
    
    # Combine the highlighted PDF and the summary PDF into a new final PDF
    final_doc = fitz.open()
    final_doc.insert_pdf(summary_doc)  # Insert summary as first pages
    final_doc.insert_pdf(fitz.open(highlighted_pdf_path))  # Insert highlighted PDF

    final_highlighted_pdf_path = "Highlighted_" + os.path.basename(pdf_path)
    final_doc.save(final_highlighted_pdf_path)

    return final_highlighted_pdf_path


# Streamlit app
def app():
    st.title("Single PDF Highlighter")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file:
        st.write("Uploaded file:", uploaded_file.name)
        color_type = {}
        num_words = st.number_input("Number of words to highlight", min_value=1, step=1)
        for i in range(num_words):
            word = st.text_input(f"Word {i+1}")
            color_name = st.selectbox(f"Pick a color for word {i+1}", list(color_options.keys()), key=i)
            if word and color_name:
                color_type[word] = color_options[color_name]

        if st.button("Highlight Words"):
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())
        
            #with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as input_tempfile:
            #    input_tempfile.write(uploaded_file.getbuffer())
            #    input_pdf_path = input_tempfile.name

            highlighted_pdf = highlight_words(uploaded_file.name, color_type)
            st.write("Highlighted PDF saved as:", highlighted_pdf)
            with open(highlighted_pdf, "rb") as file:
                btn = st.download_button(
                    label="Download Highlighted PDF",
                    data=file,
                    file_name=highlighted_pdf,
                    mime="application/pdf"
                )