import streamlit as st

st.set_page_config(page_title="Palak Piyush Desai", page_icon="images/P.png", layout="wide", initial_sidebar_state="collapsed")

st.subheader("Skillset")

skill = st.pills(
    "Skill Category",
    ["Languages", "Library", "Frameworks", "Tools"],
    default = None, 
)

if skill == "Languages":
    st.html(
        "<style>"
        ".skill_logo{" \
        "margin-bottom: 20px;}"
        "</style>"
        "<div class='imgskills'>"
        "<img class='skill_logo' src='https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E' />"
        "</div>"
        "<div class='imgskills'>"
        "<img class='skill_logo' src='https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white' /> &nbsp;"
        "</div>"
        
    )
elif skill == "Library":
    st.html(
        "<style>"
        ".skill_logo{" \
        "margin-bottom: 20px;}"
        "</style>"
        "<div class='imgskills'>"
        "<img class='skill_logo' src='https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white' /> &nbsp;"
        "</div>"
        
    )
elif skill == "Frameworks":
    st.html(
        "<style>"
        ".skill_logo{" \
        "margin-bottom: 20px;}"
        "</style>"
        "<div class='imgskills'>"
        "<img class='skill_logo' src='https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/Flask-3D72D7?style=for-the-badge&logo=flask&logoColor=white' /> &nbsp;"
        "</div>"
        
    )
elif skill == "Tools":
    st.html(
        "<style>"
        ".skill_logo{" \
        "margin-bottom: 20px;}"
        "</style>"
        "<div class='imgskills'>"
        "<img class='skill_logo' src='https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/Framer-2b2b2b?style=for-the-badge&logo=framer&logoColor=blue' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/webflow-%23146EF5.svg?style=for-the-badge&logo=webflow&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/Canva-%2300C4CC.svg?&style=for-the-badge&logo=Canva&logoColor=white' /> &nbsp;"
        "</div>"
        "<div class='imgskills'>"
        "<img class='skill_logo' src='https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=Power%20BI&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/LaTeX-47A141?style=for-the-badge&logo=LaTeX&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/Overleaf-47A141?style=for-the-badge&logo=Overleaf&logoColor=white' /> &nbsp;"
        "<img class='skill_logo' src='https://img.shields.io/badge/qgis-3.34_prizren-93b023?&style=for-the-badge&logo=qgis&logoColor=white' /> &nbsp;"
        "</div>"
        
    )
else:
    st.empty()