import os
import streamlit as st
import fitz_new

st.set_page_config(
    page_title="multi_page app",
    page_icon="")

st.title("Page in construction")
# st.success("select a page above")


def highlight_word_in_pdf(input_path, output_path, word_to_highlight):
    doc = fitz_new.open(input_path)
    # for page in doc:
    for page_num in range(len(doc)):
        page = doc[page_num]
        text_instances = []

        for word in word_to_highlight:
            text_instances.extend(page.search_for(word))
        # text_instances = page.search_for(word_to_highlight)
        for inst in text_instances:
            highlight = page.add_highlight_annot(inst)
            highlight.update()
    doc.save(output_path)


def process_pdfs(input_folder, output_folder, word_to_highlight):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)
            output_filename = f"{os.path.splitext(filename)[0]}_highlighted.pdf"
            output_path = os.path.join(output_folder, output_filename)
            highlight_word_in_pdf(input_path, output_path, word_to_highlight)
            print(f"Processed and saved: {output_path}")


# Streamlit app
def main():
    st.title("Multiple PDF Word Highlighter")

    # Input folder
    input_folder = st.text_input("Input folder path containing PDFs")

    # Output folder
    # output_folder = st.text_input("Output folder path for highlighted PDFs")
    output_folder = input_folder + '/output folder'  # "path/to/output/folder"  # Replace with your output folder path

    # Word to highlight
    word_to_highlight = st.text_input("Word to highlight in PDFs")
    # Button to start processing
    if st.button("Highlight PDFs"):
        if not input_folder or not output_folder or not word_to_highlight:
            st.error("Please provide all the required inputs.")
        else:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Process each PDF in the input folder
            for filename in os.listdir(input_folder):
                if filename.endswith(".pdf"):
                    input_path = os.path.join(input_folder, filename)
                    output_filename = f"{os.path.splitext(filename)[0]}_highlighted.pdf"
                    output_path = os.path.join(output_folder, output_filename)
                    highlight_word_in_pdf(input_path, output_path, word_to_highlight)
                    print(f"Processed and saved: {output_filename}")

            st.success(f"Highlighted PDFs have been saved to {output_folder}")

# process_pdfs(input_folder, output_folder, word_to_highlight)


if __name__ == "__main__":
    main()

