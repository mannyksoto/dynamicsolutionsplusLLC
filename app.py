"""
Dynamic Solutions Plus LLC — company website (Streamlit)
Run locally:  streamlit run app.py
"""
import streamlit as st
from site_config import BUSINESS
from ui import apply_style, footer

st.set_page_config(
    page_title=BUSINESS["name"],
    page_icon="assets/favicon.png",
    layout="wide",
)
apply_style()

pages = [
    st.Page("pages/home.py", title="Home", icon="🏡", default=True),
    st.Page("pages/services.py", title="Services", icon="💧"),
    st.Page("pages/gallery.py", title="Our Work", icon="📸"),
    st.Page("pages/about.py", title="About", icon="🌳"),
    st.Page("pages/contact.py", title="Free Estimate", icon="📞"),
]

# Top navigation bar instead of a sidebar = feels more like a normal website
nav = st.navigation(pages, position="top")
nav.run()

footer()
