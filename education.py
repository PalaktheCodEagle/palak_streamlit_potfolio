import streamlit as st

st.set_page_config(page_title="Palak Piyush Desai", page_icon="images\P.png", layout="wide", initial_sidebar_state="collapsed")


st.subheader("Education")

col1, col2 = st.columns([1,1], vertical_alignment='center')

with col1:
    st.html(
        "<style>"
        ".row{" \
        "display: inline-flex;"
        "flex-direction: row;"
        "flex-wrap: nowrap;"
        "align-content: flex-start;"
        "justify-content: flex-start;"
        "align-items: flex-start;}"
        ".column{" \
        "margin-right: 20px;}"
        "h4{" \
        "margin: 0px 0px 15px 0px}"
        "</style>"
        "<div class='education_details' style='padding: 15px; border-left: 1px #43444b solid;" \
        "font-family: monospace;'>"
        "<div class='row'>"
        "<div class='column'>" \
        " <h4 style='color: #d2d2d2; font-weight: 300;'>📍Mumbai, Maharashtra, India</h4>" 
        " <p class='degree' style='font-weight:500; color: white;'>Bachelor of Technology in Computer Engineering</p>"
        " <h4 style='color: #d2d2d2; font-weight: 300;'>K J Somaiya Institute of Technology</h4><br>"
        " <h4 style='color: #d2d2d2; font-weight: 300;'>Grade: 8.67/10</h4>"
        "</div>"
        "<div class='column'><h4 style='color: #d2d2d2; font-weight: 300;'>2021-2025</h4></div>"
        "</div>"
        "</div>"
    )

with col2:
    st.html(
        "<style>"
        ".row{" \
        "display: inline-flex;"
        "flex-direction: row;"
        "flex-wrap: nowrap;"
        "align-content: flex-start;"
        "justify-content: flex-start;"
        "align-items: flex-start;}"
        ".column{" \
        "margin-right: 20px;}"
        "h4{" \
        "margin: 0px 0px 15px 0px}" \
        "</style>"
        "<div class='education_details' style='padding: 15px; border-left: 1px #43444b solid;" \
        "font-family: monospace;'>"
        "<div class='row'>"
        "<div class='column'>" \
        " <h4 style='color: #d2d2d2; font-weight: 300;'>📍Thane, Maharashtra, India</h4>" 
        " <p class='degree' style='font-weight:500; color: white;'>Higher Secondary Certificate in Science</p>"
        " <h4 style='color: #d2d2d2; font-weight: 300;'>Matoshree Prabodhini Jr. College of Science</h4><br>"
        " <h4 style='color: #d2d2d2; font-weight: 300;'>Cleared 12th grade with 93.67%.</h4>"
        "</div>"
        "<div class='column'><h4 style='color: #d2d2d2; font-weight: 300; margin: 0;'>2019-2021</h4></div>"
        "</div>"
        "</div>"
    )

st.html("<br>")

col3, col4 = st.columns([1,1], vertical_alignment='center')

with col3:
    st.html(
        "<style>"
        ".row{" \
        "display: inline-flex;"
        "flex-direction: row;"
        "flex-wrap: nowrap;"
        "align-content: flex-start;"
        "justify-content: flex-start;"
        "align-items: flex-start;}"
        ".column{" \
        "margin-right: 20px;}"
        "h4{" \
        "margin: 0px 0px 15px 0px}" \
        "</style>"
        "<div class='education_details' style='padding: 15px; border-left: 1px #43444b solid;" \
        "font-family: monospace;'>"
        "<div class='row'>"
        "<div class='column'>" \
        " <h4 style='color: #d2d2d2; font-weight: 300;'>📍Thane, Maharashtra, India</h4>" 
        " <p class='degree' style='font-weight:500; color: white;'>Secondary School Certificate</p>"
        " <h4 style='color: #d2d2d2; font-weight: 300;'>K.E.S's Bhagavati Vidyalaya</h4><br>"
        " <h4 style='color: #d2d2d2; font-weight: 300;'>Cleared 10th grade with 91.2%.</h4>"
        "</div>"
        "<div class='column'><h4 style='color: #d2d2d2; font-weight: 300; margin: 0;'>2007-2019</h4></div>"
        "</div>"
        "</div>"
    )