import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Set Streamlit page configuration (must be first Streamlit command)
st.set_page_config(page_title="Biography ni Enzo", layout="wide")

# Page setup
about_page = st.Page(
    page="views/2_Home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)
project_1_page = st.Page(
    page="views/3_About_me.py",
    title="About Me",
    icon=":material/account_circle:",
)
project_2_page = st.Page(
    page="views/4_Educational_Attainment.py",
    title="Educational Attainment",
    icon=":material/school:",
)
project_3_page = st.Page(
    page="views/5_Hobbies.py",
    title="My Hobbies",
    icon=":material/favorite:",
)

# Navigation
pg = st.navigation(pages=[about_page, project_1_page, project_2_page, project_3_page])
pg.run()