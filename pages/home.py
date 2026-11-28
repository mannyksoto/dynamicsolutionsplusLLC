import streamlit as st
from site_config import BUSINESS, SERVICES, WHY_US
from ui import call_to_action, image_b64

phone_digits = "".join(c for c in BUSINESS["phone"] if c.isdigit())
FB_ICON = ('<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">'
           '<circle cx="12" cy="12" r="12" fill="#1877F2"/>'
           '<path fill="#fff" d="M13.4 19v-6h2l.3-2.4h-2.3V9.1c0-.7.2-1.2 1.2-1.2h1.3V5.8'
           'c-.2 0-1-.1-1.9-.1-1.9 0-3.1 1.1-3.1 3.2v1.8H8.8V13h2.1v6z"/></svg>')
fb_button = (f'<a class="btn btn-fb" href="{BUSINESS["facebook"]}" target="_blank">'
             f'{FB_ICON} Follow us on Facebook</a>') if BUSINESS.get("facebook") else ""

st.markdown(
    f"""<div class="hero"><div class="hero-grid">
    <div class="hero-logo"><img src="{image_b64('assets/logo.jpg')}" alt="{BUSINESS['name']} logo"></div>
    <div class="hero-text">
      <div class="area">📍 Serving {BUSINESS['service_area']}</div>
      <div class="actions">
        <a class="btn btn-primary" href="tel:{phone_digits}">Call {BUSINESS['phone']}</a>
        <span class="btn badge">✓ {BUSINESS['license_note']}</span>
              <div class="actions fb-row">{fb_button}</div>
      </div>
    </div>
    </div></div>""",
    unsafe_allow_html=True,
)

st.page_link("pages/contact.py", label="Get a Free Estimate", icon="📞")

st.subheader("What we do")
cards = "".join(
    f"""<a class="card-link" href="services" target="_self"><div class="card">
    <div class="icon">{svc['icon']}</div><h3>{svc['title']}</h3><p>{svc['blurb']}</p>
    <span class="more">Learn more →</span></div></a>"""
    for svc in SERVICES
)
st.markdown(f'<div class="card-grid">{cards}</div>', unsafe_allow_html=True)
st.write("")

st.subheader("Why homeowners choose us")
cols = st.columns(len(WHY_US))
for col, (icon, text) in zip(cols, WHY_US):
    col.markdown(f"### {icon}\n**{text}**")

call_to_action()
