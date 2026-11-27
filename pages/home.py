import streamlit as st
from site_config import BUSINESS, SERVICES, WHY_US
from ui import call_to_action

st.markdown(
    f"""<div class="hero">
    <h1>{BUSINESS['name']}</h1>
    <p>{BUSINESS['tagline']} · Serving {BUSINESS['service_area']}</p>
    <p>📞 <b>{BUSINESS['phone']}</b> &nbsp;|&nbsp; {BUSINESS['license_note']}</p>
    </div>""",
    unsafe_allow_html=True,
)

c1, c2 = st.columns([1, 1])
with c1:
    st.page_link("pages/contact.py", label="Get a Free Estimate", icon="📞")
with c2:
    st.page_link("pages/services.py", label="See Our Services", icon="💧")

st.subheader("What we do")
cols = st.columns(len(SERVICES))
for col, svc in zip(cols, SERVICES):
    with col:
        st.markdown(
            f"""<div class="card"><div class="icon">{svc['icon']}</div>
            <h3>{svc['title']}</h3><p>{svc['blurb']}</p></div>""",
            unsafe_allow_html=True,
        )

st.subheader("Why homeowners choose us")
cols = st.columns(len(WHY_US))
for col, (icon, text) in zip(cols, WHY_US):
    col.markdown(f"### {icon}\n**{text}**")

call_to_action()
