import streamlit as st
from PIL import Image

st.set_page_config(page_title="Palak Piyush Desai", page_icon="images\P.png", layout="wide", initial_sidebar_state="auto")

col1, col2, col3 = st.columns([1,2,2], vertical_alignment='center')
my_logo = "images\P.png"

with col1:
    html_code = """
    <div style="text-align: center;">
    <img src="https://i.pinimg.com/736x/68/4c/b6/684cb636cf67568ed031a5fee627c8a5.jpg"
         alt="Profile Image"
         width="200"
         style="border-radius: 50%;">
        </div>
        """

    st.html(html_code)

with col2:
    st.html(
        "<style>" \
        "button{" \
        "background-color: #15171f;"
        "border: 1px #43444b solid;"
        "border-radius: 8px;"
        "box-sizing: border-box;"
        "padding: 7px 12px 7px 12px;"
        "width: fit-content;}"
        ".btndiv{" \
        "color: white;" \
        "text-decoration: none;}"        
        "@media (min-width: 300px) and (max-width: 640px){" \
        "h1,h3, h6{" \
        "text-align: center;}" \
        ".abtn{" \
        "text-align: center;}}"
        "</style>"
        "<div class='details'>"
        "<h1 style='font-size: 1.7rem'>Palak Piyush Desai</h1>"
        "<h3 style='margin-top:-1rem; font-size: 0.9rem'>Passionate & Creative Developer</h3>"
        "<h3 style='font-size: 0.8rem'>📍India</h3>"
        "<div class='mybtn'>"
        "<div class='abtn' style='margin-bottom: 10px'><button><a class='btndiv' href='mailto:palakd683@gmail.com' " \
        "target=_blank>📧 Mail</a></button></div>"
        "<div class='abtn' style='margin-bottom: 10px'><button><a class='btndiv' href='https://drive.google.com/file/d/11LgmxgbEpYjGpVL2X4O9OdeWl1bfSJBv/view' " \
        "target=_blank>⬇️ Download Resume</a></button></div>"
        "</div>"
        "</div>"
    )

with col3:
    st.html(
        "<style>"
        "button{" \
        "background-color: #15171f;"
        "border: 1px #43444b solid;"
        "border-radius: 8px;"
        "box-sizing: border-box;"
        "padding: 7px 12px 7px 12px;"
        "width: fit-content;}"
        ".btndiv{" \
        "color: white;" \
        "text-decoration: none;}" \
        "img{" \
        "border-radius: 20px}" \
        ".allbtn{" \
        "text-align: end;}"
        "@media (min-width: 300px) and (max-width: 640px){" \
        "h1,h3, h6{" \
        "text-align: center;}" \
        ".abtn{" \
        "text-align: center;}"
        ".abtn{" \
        "margin:10px;" \
        "}" \
        ".allbtn{" \
        "display: inline-flex;" \
        "font-size: 0.8em;" \
        "width: 100%;"
        "text-align: center;"
        "justify-content: center;" \
        "flex-wrap: wrap;" \
        "}" \
        ".logo{" \
        "width: 10px;" \
        "height:10px;}}"
        "</style>"
        "<div class='allbtn'>"
        "<div class='abtn'><button><a class='btndiv' href='https://www.linkedin.com/in/palak-desai-21180a25b/' " \
        "target=_blank><img class='logo' src='https://i.pinimg.com/736x/75/d2/ca/75d2ca104a1903bc305fa6eed718012d.jpg' width=20 height=20>" \
        " LinkedIn</a></button></div><br>"
        "<div class='abtn'><button><a class='btndiv' href='https://github.com/PalaktheCodEagle' " \
        "target=_blank><img class='logo' src='https://i.pinimg.com/736x/b2/c4/69/b2c46907798def8a6859d19c46d37b27.jpg' width=20 height=20>" \
        " Github</a></button></div><br>"
        "<div class='abtn'><button><a class='btndiv' href='https://x.com/PalakD36' " \
        "target=_blank><img class='logo' src='https://i.pinimg.com/1200x/b2/68/83/b268838fe5a0c0ca504c2fc103843ae3.jpg' width=20 height=20>" \
        " Twitter</a></button></div><br>"
        "<div class='abtn'><button><a class='btndiv' href='https://medium.com/@palakd683' " \
        "target=_blank><img class='logo' src='https://i.pinimg.com/1200x/45/c8/4a/45c84aafac55cabf316c0f2ff65cc798.jpg' width=20 height=20>" \
        " Medium</a></button></div>"
        "</div>"
    )
st.html(
    "<hr style='width: 100%;'>"
)

pages = {
    "About Me": [
        st.Page("about.py", title="About", icon="👧🏻"),
    ],
    "Education": [
        st.Page("education.py", title="Education", icon="🏫"),
    ],
    "Skills": [
        st.Page("skills.py", title="Skills", icon="👩🏻‍💻"),
    ],
    "Experience and Work": [
        st.Page("experience.py", title="Experience", icon="📊"),
        st.Page("projects.py", title="Projects", icon="📱"),
        st.Page("publications.py", title="Publications", icon="📖"),
    ],
    "Merits": [
        st.Page("merits.py", title="Certifications", icon="🎖️"),
        st.Page("cocurricularact.py", title="Co-Curricular Activity", icon="⚙️"),
        st.Page("achieve.py", title="Achievements", icon="🌟"),
    ],
}

pg = st.navigation(pages)
st.logo(my_logo)
pg.run()