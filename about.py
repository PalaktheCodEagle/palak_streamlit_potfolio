import streamlit as st

st.set_page_config(page_title="Palak Piyush Desai", page_icon="images\P.png", layout="wide", initial_sidebar_state="auto")

st.subheader("About Me")
st.html(
    "<div class='aboutme' style='background-color: #1a1c24; padding: 15px; border-radius: 10px;" \
    "font-family: monospace;'>"
    "• I'm a tech and design enthusiast passionate about Web Development, UI/UX design, and Data Analytics.<br>" 
    "• I love exploring the intersection of creativity and technology.<br>"
    "• I enjoy creating intuitive, beautiful user interfaces, bringing them to life with functional web development,"
    " and analyzing data to drive insights.<br>" 
    "• I'm dedicated to continuous learning and making impactful, user-centered solutions.<br>"
    "</div>"
)
