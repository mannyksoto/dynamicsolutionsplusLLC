import streamlit as st
from site_config import BUSINESS, SERVICES, WHY_US
from ui import call_to_action, image_b64

phone_digits = "".join(c for c in BUSINESS["phone"] if c.isdigit())

st.markdown(
    f"""<div class="hero"><div class="hero-grid">
    <div class="hero-logo"><img src="{image_b64('assets/logo.jpg')}" alt="{BUSINESS['name']} logo"></div>
    <div class="hero-text">
      <div class="area">📍 Serving {BUSINESS['service_area']}</div>
      <div class="actions">
        <a class="btn btn-primary" href="tel:{phone_digits}">Call {BUSINESS['phone']}</a>
        <span class="btn badge">✓ {BUSINESS['license_note']}</span>
      </div>
    </div>
    </div></div>""",
    unsafe_allow_html=True,
)

st.page_link("pages/contact.py", label="Get a Free Estimate", icon="📞")

st.subheader("What we do")
per_row = 4 if len(SERVICES) <= 4 else 3
for i in range(0, len(SERVICES), per_row):
    cols = st.columns(per_row)
    for col, svc in zip(cols, SERVICES[i:i + per_row]):
        col.markdown(
            f"""<div class="card"><div class="icon">{svc['icon']}</div>
            <h3>{svc['title']}</h3><p>{svc['blurb']}</p></div>""",
            unsafe_allow_html=True,
        )
    st.write("")

st.subheader("Why homeowners choose us")
cols = st.columns(len(WHY_US))
for col, (icon, text) in zip(cols, WHY_US):
    col.markdown(f"### {icon}\n**{text}**")

call_to_action()
