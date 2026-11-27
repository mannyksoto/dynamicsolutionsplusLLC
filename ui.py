"""Shared styling + header/footer used by every page."""
import streamlit as st
from site_config import BUSINESS

CSS = """
<style>
/* hide Streamlit chrome so it looks like a normal website */
#MainMenu, footer, header [data-testid="stToolbar"] {visibility: hidden;}
.block-container {padding-top: 2rem; max-width: 1100px;}

.hero {
  background: linear-gradient(135deg, #1f4d2b 0%, #2e7d4f 60%, #3a8fb7 100%);
  color: #fff; border-radius: 16px; padding: 3rem 2rem; margin-bottom: 2rem;
}
.hero h1 {color:#fff; font-size: 2.6rem; margin-bottom: .3rem;}
.hero p  {font-size: 1.2rem; opacity: .95;}

.card {
  background: #ffffff; border: 1px solid #e3ebe5; border-radius: 14px;
  padding: 1.4rem; height: 100%; box-shadow: 0 2px 8px rgba(0,0,0,.04);
}
.card h3 {margin-top: .2rem; color: #1f4d2b;}
.icon {font-size: 2rem;}

.cta {
  background: #f1f7f3; border-left: 6px solid #2e7d4f;
  border-radius: 10px; padding: 1.2rem 1.5rem; margin: 2rem 0;
}
.site-footer {
  text-align: center; color: #6b7a70; font-size: .9rem;
  border-top: 1px solid #e3ebe5; margin-top: 3rem; padding-top: 1rem;
}
</style>
"""


def apply_style():
    st.markdown(CSS, unsafe_allow_html=True)


def call_to_action():
    st.markdown(
        f"""<div class="cta"><b>Ready for a better yard?</b>
        Call <b>{BUSINESS['phone']}</b> or request a free estimate on the Contact page.</div>""",
        unsafe_allow_html=True,
    )


def footer():
    links = []
    if BUSINESS["facebook"]:
        links.append(f'<a href="{BUSINESS["facebook"]}" target="_blank">Facebook</a>')
    if BUSINESS["instagram"]:
        links.append(f'<a href="{BUSINESS["instagram"]}" target="_blank">Instagram</a>')
    social = " · ".join(links)
    st.markdown(
        f"""<div class="site-footer">
        <b>{BUSINESS['name']}</b> · {BUSINESS['phone']} · {BUSINESS['email']}<br>
        Serving {BUSINESS['service_area']} · {BUSINESS['license_note']}<br>{social}
        </div>""",
        unsafe_allow_html=True,
    )
