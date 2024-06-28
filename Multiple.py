import streamlit as st
import fitz 
import os
from pathlib import Path


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


# Highlight words in a PDF
def highlight_pdf(input_path, output_path, words_of_interest):
    doc = fitz.open(input_path)
    for page in doc:
        for word, color in words_of_interest.items():
            text_instances = page.search_for(word)
            for inst in text_instances:
                highlight = page.add_highlight_annot(inst)
                highlight.set_colors(stroke=color)  # Set highlight color
                highlight.update()
    doc.save(output_path)

# Access PDF in input and output folder to highlight
def process_pdfs(input_folder, output_folder, words_of_interest):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)
            output_filename = f"{os.path.splitext(filename)[0]}_highlighted.pdf"
            output_path = os.path.join(output_folder, output_filename)
            highlight_pdf(input_path, output_path, words_of_interest)
            print(f"Processed and saved: {output_path}")



# Streamlit app
def app():
    st.title("Multiple PDF Highlighter")

    # Specify the input and create an outut folder
    input_folder = st.text_input("Enter the path to the folder containing PDFs")
    output_ = input_folder + '/output folder'  # "path/to/output/folder"  # Replace with your output folder path
    output_folder = os.path.join(input_folder, output_)

    # Input the words
    st.write("Enter words to highlight and their corresponding colors:")
    #words_input = st.text_area("Words (comma-separated, e.g., word1: #ff0000, word2: #00ff00)")

    # Match words of interest with colors
    words_of_interest = {}
    num_words = st.number_input("Number of words to highlight", min_value=1, step=1)
    for i in range(num_words):
        word = st.text_input(f"Word {i+1}")
        color_name = st.selectbox(f"Pick a color for word {i+1}", list(color_options.keys()))
        if word and color_name:
            words_of_interest[word] = color_options[color_name]
    
    # Process PDFs
    if st.button("Highlight PDFs"):
        if not input_folder or not word:
            st.error("Please provide all necessary inputs.")
        else:
            pdf_files = list(Path(input_folder).glob("*.pdf"))
            total_pdfs = len(pdf_files)
            st.write(f"Found {total_pdfs} PDF files in the input folder.")
            

            progress_bar = st.progress(0)
            processed_count = 0

            #pdf_files=os.listdir(uploaded_folder)
            if not pdf_files:
                st.error("No PDF files found in the specified folder.")
            else:
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                    #process_pdfs(uploaded_folder, output_folder, words_to_highlight)

                for filename in os.listdir(input_folder):
                    if filename.endswith(".pdf"):
                        input_path = os.path.join(input_folder, filename)
                        output_filename = f"{os.path.splitext(filename)[0]}_highlighted.pdf"
                        output_path = os.path.join(output_folder, output_filename)
                        highlight_pdf(input_path, output_path, words_of_interest)
                        processed_count += 1
                        progress_bar.progress(processed_count / total_pdfs)
                        st.write(f"Processed {processed_count}/{total_pdfs} PDFs")
                st.success(f"Highlighting completed for {processed_count} PDFs.")

