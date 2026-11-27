import streamlit as st
from site_config import BUSINESS, ABOUT_TEXT, WHY_US
from ui import call_to_action

st.title(f"About {BUSINESS['short_name']}")
st.markdown(ABOUT_TEXT)

st.subheader("Our promise")
for icon, text in WHY_US:
    st.markdown(f"{icon} **{text}**")

st.subheader("Hours & service area")
st.write(f"🕒 {BUSINESS['hours']}")
st.write(f"📍 {BUSINESS['service_area']}")

call_to_action()
