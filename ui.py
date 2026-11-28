"""Shared styling + header/footer used by every page."""
import base64
from pathlib import Path
import streamlit as st
from site_config import BUSINESS

CSS = """
<style>
/* hide Streamlit chrome so it looks like a normal website */
#MainMenu, footer, [data-testid="stToolbarActions"], [data-testid="stMainMenu"], [data-testid="stAppDeployButton"] {display: none !important;}
.block-container {padding-top: 2rem; max-width: 1300px;}

/* phone: label the collapsed menu button so visitors know to tap it */
[data-testid="stExpandSidebarButton"] {
  display: inline-flex !important; align-items: center; gap: .35rem;
  width: auto !important; padding: .35rem .8rem !important;
  border: 1.5px solid #2e7d4f !important; border-radius: 999px !important;
  background: #f1f7f3 !important; color: #1f4d2b !important;
}
[data-testid="stExpandSidebarButton"]::after {
  content: "Menu"; font-weight: 600; font-size: .95rem;
}

.hero {
  background: linear-gradient(135deg, #1f4d2b 0%, #2e7d4f 30%, #3d1a5c 100%);
  color: #fff; border-radius: 16px; padding: 1.75rem; margin-bottom: 2rem;
}
.hero-grid {
  display: grid; grid-template-columns: 1.45fr 1fr; gap: 2rem; align-items: center;
}
.hero-logo img {
  width: 100%; border-radius: 12px; display: block;
  box-shadow: 0 10px 30px rgba(0,0,0,.35);
}
.hero-text {text-align: center;}
.hero .hero-title {font-size: 2.2rem; font-weight: 700; line-height: 1.15; margin-bottom: .6rem;}
.hero .tagline {font-size: 1.35rem; font-style: italic; color: #FEBE01; font-weight: 600; margin-bottom: .5rem;}
.hero .area {font-size: 1.3rem; opacity: .95; margin-bottom: 1.8rem;}
.hero .actions {display: flex; gap: .8rem; justify-content: center; flex-wrap: wrap;}
.hero .btn {
  display: inline-block; padding: .7rem 1.4rem; border-radius: 999px;
  font-weight: 700; text-decoration: none !important; font-size: 1.05rem;
}
.hero .btn-primary {background: #FEBE01; color: #111 !important;}
.hero .btn-primary:hover {background: #ffd23f;}
.hero .badge {
  border: 1.5px solid rgba(255,255,255,.6); color: #fff;
  background: rgba(255,255,255,.08);
}
@media (max-width: 900px) {
  .hero {padding: 1.5rem;}
  .hero-grid {grid-template-columns: 1fr; gap: 1.5rem;}
  .hero .hero-title {font-size: 2rem;}
}

.card {
  background: #ffffff; border: 1px solid #e3ebe5; border-radius: 14px;
  padding: 1.4rem; height: 100%; box-shadow: 0 2px 8px rgba(0,0,0,.04);
}
.card h3 {
  margin-top: .2rem; color: #1f4d2b; line-height: 1.25;
  font-size: clamp(1.15rem, 1.7vw, 1.5rem) !important;
  word-break: keep-all; overflow-wrap: normal; hyphens: none;
}
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
        Call <b>{BUSINESS['phone']}</b> or request a free estimate online.</div>""",
        unsafe_allow_html=True,
    )
    st.page_link("pages/contact.py", label="Request a Free Estimate", icon="📞")


def footer():
    links = []
    if BUSINESS.get("facebook"):
        links.append(f'<a href="{BUSINESS["facebook"]}" target="_blank">Facebook</a>')
    social = " · ".join(links)
    st.markdown(
        f"""<div class="site-footer">
        <b>{BUSINESS['name']}</b> · {BUSINESS['phone']} · {BUSINESS['email']}<br>
        Serving {BUSINESS['service_area']} · {BUSINESS['license_note']}<br>{social}
        </div>""",
        unsafe_allow_html=True,
    )


@st.cache_data
def image_b64(relative_path: str) -> str:
    """Return an image as a data: URL so it can be used inside custom HTML."""
    path = Path(__file__).parent / relative_path
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()