import streamlit as st
from os.path import join
from PIL import Image
# from styles import custom_style

st.set_page_config(
    page_title="Homepage",
    page_icon="🖐")

# Get images
logo = Image.open(join("img", "highlighter.jpg"))
icon = Image.open(join("img", "highlighter.jpg"))

# streamlit_style('Microorganism Detection in Water', layout='wide', page_icon=icon)

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)


def main():
    st.title("PDF auto highlighter")
    col1, col2 = st.columns(2)

    with col1:
        st.image(logo)

    with col2:
        st.subheader("Description")
        st.write("This web app inputs a single PDF, or multiple PDF, and a desired search word, then highlights \
                 all instances of the word")

        # st.subheader("Dataset")
        # st.write("The overall dataset is made up of the following two datasets:")
        # st.markdown("- Environmental Microorganism Image Dataset Seventh Version is a microscopic image data set \
        #            containing 41 types of EMs, with 2,65 images and 13,216 labeled objects in XML Format.")

        # st.markdown("- Environmental Microorganism Image Dataset Sixth Version is a microscopic image data set containing \
        #        21 types of EMs. Each type of EM contains 40 original and 40 GT images, in total 1680 EM ages. \
        #        Box annotations were generated using the Roboflow tool, generating XML and YoloV8 files.") '''

    st.write("© 2024 HLNUG. All rights reserved.")


if __name__ == '__main__':
    main()