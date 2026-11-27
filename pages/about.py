import streamlit as st
from site_config import BUSINESS, ABOUT_TEXT, TRIBUTE_TEXT, WHY_US
from ui import call_to_action

st.title(f"About {BUSINESS['short_name']}")
st.markdown(ABOUT_TEXT)

st.write("")
with st.container(border=True):
    st.subheader("In Memory of Brad Mason")
    st.caption("Founder · 2021")
    st.markdown(TRIBUTE_TEXT)

st.subheader("Our promise")
for icon, text in WHY_US:
    st.markdown(f"{icon} **{text}**")

st.subheader("Hours & service area")
st.write(f"🕒 {BUSINESS['hours']}")
st.write(f"📍 {BUSINESS['service_area']}")

call_to_action()