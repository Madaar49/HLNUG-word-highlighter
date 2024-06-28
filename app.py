import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
        page_title="Highlighter app",
         layout="centered"
         )

# Importing pages 
import Single, Multiple, Homepage, About


# Menu design
with st.sidebar:        
    selected = option_menu(
        menu_title='Navigation Menu',
        options=['Home','Single','Multiple','About'],
        icons=['house-fill','file-earmark-pdf','folder2-open','info-circle-fill'],
        menu_icon='chat-text-fill',
        default_index=1,
        styles={
            "container": {"padding": "5!important","background-color":'black'},
            "icon": {"color": "white", "font-size": "30px"}, 
            "nav-link": {"color":"white","font-size": "22px", "text-align": "left",
                "margin":"0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},}
                )

# Pages            
if selected == "Home":
    Homepage.app()
if selected == "Single":
    Single.app()    
if selected == "Multiple":
    Multiple.app()      
if selected == "About":
    About.app()        
