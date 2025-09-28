import streamlit as st

st.set_page_config(page_title="Palak Piyush Desai", page_icon="images\P.png", layout="wide", initial_sidebar_state="collapsed")

st.subheader("Achievements")

categories = st.pills(
    "Achievement Category",
    ["Copyright", "Letter of Appreciation (LOA)", "Competition"],
    default = None,
)

if categories == "Copyright":
    with st.expander("Literary/Dramatic Work - Copyright Office, Government of India"):
        st.html(
            "<strong>Description:</strong>"
            "<p>Successfully registered and copyrighted following two institute projects at Copyright Office, Government of India:</p>"
            "<p>• The User Manual developed for project 'Virtual Lab of Operating Systems.'"
            "<p>• The User Manual developed for project 'KJSIT's Stakeholder's Feedback Analysis Portal.'</p>"
        )
    with st.expander("Computer Software Work - Copyright Office, Government of India"):
        st.html(
            "<strong>Description:</strong>"
            "<p>Successfully registered and copyrighted following two institute projects at Copyright Office, Government of India:</p>"
            "<p>• Software 'Efficient Housing Society Management Solutions' developed for the client 'Moraj Residency.'"
            "<p>• Software model 'AQI Prediction For Maharashtra Districts Using GRU-GCN Ensembled Model' developed for the project"
            " 'LULC Transformation and Urban Expansion Analysis in Mumbai and Satara.'</p>"
        )
elif categories == "Letter of Appreciation (LOA)":
    with st.expander("Institute Projects - Letter of Appreciation (LOA)"):
        st.html(
            "<strong>Description:</strong>"
            "<p>Received LOA from the institute for successful completion and deployment of two following institute projects:</p>"
            "<p>• Virtual Lab of Operating Systems."
            "<p>• KJSIT's Feedback Analysis Portal.</p>"
        )
elif categories == "Competition":
    with st.expander("INTECH 2K24 - National Level Poster-cum-Project Competition"):
        st.html(
            "<strong>Description:</strong>"
            "<p>Received special prize from the institute for winning a national project competition:</p>"
            "<p>• Special Prize Awardee for project 'CivicSynergy: Streamlining Housing Society Management System.'</p>"
        )
else:
    st.empty()