import streamlit as st
import fitz_new 
import os


# Function to highlight a word in a PDF
def highlight_word_in_pdf(input_pdf, word, output_path):
    doc = fitz_new.open(stream=input_pdf.read(), filetype="pdf")
    for page in doc:
        text_instances = page.search_for(word)
        for inst in text_instances:
            highlight = page.add_highlight_annot(inst)
            highlight.update()
    doc.save(output_path)


# Streamlit app
def main():
    st.title("PDF Word Highlighter")

    # File uploader for PDF
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    # Word to highlight
    word_to_highlight = st.text_input("Word to highlight in the PDF")

    # Button to start processing
    if st.button("Highlight PDF"):
        if uploaded_file is None or not word_to_highlight:
            st.error("Please upload a PDF file and provide a word to highlight.")
        else:
            # Create an output directory
            output_folder = "highlighted_pdfs"
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Define the output file path
            original_filename = os.path.splitext(uploaded_file.name)[0]
            output_filename = f"{original_filename}_highlight.pdf"
            output_path = os.path.join(output_folder, output_filename)

            # Highlight the word in the PDF and save it
            highlight_word_in_pdf(uploaded_file, word_to_highlight, output_path)

            st.success(f"Highlighted PDF has been saved as {output_filename} in {output_folder}")
            with open(output_path, "rb") as file:
                btn = st.download_button(
                    label="Download highlighted PDF",
                    data=file,
                    file_name=output_filename,
                    mime="application/pdf"
                )

if __name__ == "__main__":
    main()

