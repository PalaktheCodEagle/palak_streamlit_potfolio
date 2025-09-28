import streamlit as st

st.set_page_config(page_title="Palak Piyush Desai", page_icon="images/P.png", layout="wide", initial_sidebar_state="collapsed")

st.subheader("Projects")

with st.expander("LULC Transformation and Urban Expansion Analysis in Mumbai and Satara"):
    st.image("images/lulc.png", width=500 )
    st.html(
        "<strong>Domain:</strong> Web + Analytical"
    )
    st.html(
            "<strong>Duration:</strong> Jul 2024 - May 2025"
        )
    st.html(
        "<strong>Description:</strong>"
        "<p>Analysis of Land Use Land Cover (LULC) changes in Mumbai and Satara regions using Google Earth Engine and QGIS (MOLUSCE)"
        "for LULC classification and future land cover predictions, further integration of  Explainable AI (XAI) to interpret the impact"
         "of LULC features on environmental outcomes, a GRU+GCN model to forecast air quality and finally the use of"
         "Composite-Kernel Gaussian Process Regression (GPR) for diphtheria risk.</p>"
    )

with st.expander("CivicSynergy: Streamlining Housing Society Management"):
    st.image("images/moraj.png", width=500 )
    st.link_button("Visit Site", "http://morajresidency.co.in/")
    st.html(
        "<strong>Domain:</strong> Web"
    )
    st.html(
            "<strong>Duration:</strong> Jan 2024 - Jun 2024"
        )
    st.html(
        "<strong>Description:</strong>"
        "<p>A Housing Society Management System (HSMS) to streamline administrative tasks and enhance resident experiences.</p>"
    )

with st.expander("KJSIT's Student Achievement Portal with OCR tool"):
    st.image("images/ocr.png", width=500 )
    st.html(
        "<strong>Domain:</strong> Web"
    )
    st.html(
            "<strong>Duration:</strong> Jul 2023 - Dec 2023"
        )
    st.html(
        "<strong>Description:</strong>"
        "<p>An Optical Character Recognition (OCR) tool integrated with certificate management in education for accurate data extraction.</p>"
    )
    
with st.expander("KJSIT's Stakeholders Feedback Analysis Portal"):
    st.image("images/feedback.png", width=500 )
    st.link_button("Visit Site", "https://feedbackportal.kjsieit.in/new/")
    st.html(
        "<strong>Domain:</strong> Web"
    )
    st.html(
            "<strong>Duration:</strong> Jan 2023 - Jul 2023"
        )
    st.html(
        "<strong>Description:</strong>"
        "<p>A web-based system to improve communication and collaboration between institutions and stakeholders, crucial for accreditation.</p>"
    )

with st.expander("Virtual Lab of Operating Systems"):
    st.image("images/vlab.png", width=500 )
    st.link_button("Visit Site", "https://vlabcomp.kjsieit.in/")
    st.html(
        "<strong>Domain:</strong> Web"
    )
    st.html(
            "<strong>Duration:</strong> Jul 2022 - Dec 2022"
        )
    st.html(
        "<strong>Description:</strong>"
        "<p>A Virtual Lab for Operating Systems, an e-learning tool to explore operating system algorithms through theory, " \
        "examples, flowcharts, quizzes, and code implementation.</p>"
    )