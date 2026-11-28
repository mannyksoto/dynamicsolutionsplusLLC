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
.hero .area {font-size: 1rem; opacity: .9; margin-bottom: 1.6rem;}
.hero .actions {display: flex; gap: .8rem; justify-content: center; flex-wrap: wrap;}
.hero .btn {
  display: inline-block; padding: .7rem 1.4rem; border-radius: 999px;
  font-weight: 700; text-decoration: none !important; font-size: 1.05rem;
}
.hero .btn-primary {background: #FEBE01; color: #111 !important;}
.hero .btn-primary:hover {background: #ffd23f;}
.hero .btn-fb {
  background: #fff; color: #1877F2 !important;
  display: inline-flex; align-items: center; gap: .5rem;
}
.hero .btn-fb:hover {background: #eef3fe;}
.hero .fb-row {margin-top: .8rem;}

.hero .badge {
  border: 1.5px solid rgba(255,255,255,.6); color: #fff;
  background: rgba(255,255,255,.08);
}
@media (max-width: 900px) {
  .hero {padding: 1.5rem;}
  .hero-grid {grid-template-columns: 1fr; gap: 1.5rem;}
  .hero .hero-title {font-size: 2rem;}
}

/* ---------- brand colors ---------- */
/* green #2e7d4f · dark green #1f4d2b · purple #3d1a5c · gold #FEBE01 */

/* page titles: banner-style header strip */
[data-testid="stHeading"] h1 {
  background: linear-gradient(135deg, #1f4d2b 0%, #2e7d4f 30%, #3d1a5c 100%);
  color: #fff !important; border-radius: 14px; padding: 1.1rem 1.5rem !important;
  border-bottom: 5px solid #FEBE01; margin-bottom: 1rem;
}
/* hide the little link icons Streamlit adds next to headings */
[data-testid="stHeaderActionElements"] {display: none !important;}

/* section headings: gold underline accent */
[data-testid="stHeading"] h3 {
  color: #3d1a5c; display: inline-block;
  border-bottom: 4px solid #FEBE01; padding-bottom: .2rem !important;
}

/* cards: gradient strip on top, gold bullets, icon in a soft circle */
.card {
  position: relative; overflow: hidden;
  background: #ffffff; border: 1px solid #e3ebe5; border-radius: 14px;
  padding: 1.6rem 1.4rem 1.4rem; height: 100%; box-shadow: 0 4px 14px rgba(31,77,43,.08);
  transition: transform .15s ease, box-shadow .15s ease;
}
.card::before {
  content: ""; position: absolute; top: 0; left: 0; right: 0; height: 6px;
  background: linear-gradient(90deg, #2e7d4f, #3d1a5c);
}
.card:hover {transform: translateY(-3px); box-shadow: 0 10px 24px rgba(61,26,92,.15);}
.card h3 {
  margin-top: .2rem; color: #1f4d2b; line-height: 1.25;
  font-size: clamp(1.15rem, 1.7vw, 1.5rem) !important;
  word-break: keep-all; overflow-wrap: normal; hyphens: none;
}
.card li::marker {color: #FEBE01; font-size: 1.2em;}
/* clickable cards on the Home page */
.card-link, .card-link:hover {text-decoration: none !important; color: inherit !important; display: block; height: 100%;}
.card-link .card {display: flex; flex-direction: column; min-height: 100%;}
.card-link .card p {color: #1d2b22;}
.card .more {margin-top: auto; padding-top: .6rem; font-weight: 600; color: #2e7d4f;}
.card-link:hover .more {color: #3d1a5c;}
/* Home page cards: one grid, equal heights, wraps on smaller screens */
.card-grid {display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 1rem;}
.card-grid .card-link .card {height: 100%;}

/* clickable cards on the Home page */
.card-link, .card-link:hover {text-decoration: none !important; color: inherit !important; display: block; height: 100%;}
.card-link .card {display: flex; flex-direction: column; min-height: 100%;}
.card-link .card p {color: #1d2b22;}
.card .more {margin-top: auto; padding-top: .6rem; font-weight: 600; color: #2e7d4f;}
.card-link:hover .more {color: #3d1a5c;}
/* Home page cards: one grid, equal heights, wraps on smaller screens */
.card-grid {display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 1rem;}
.card-grid .card-link .card {height: 100%;}
.icon {
  font-size: 1.8rem; width: 3.2rem; height: 3.2rem; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  background: linear-gradient(135deg, #e6f2ea, #ece4f3);
}

/* call-to-action box: banner gradient with gold phone number */
.cta {
  background: linear-gradient(135deg, #1f4d2b 0%, #2e7d4f 35%, #3d1a5c 100%);
  color: #fff; border-radius: 14px; padding: 1.3rem 1.6rem; margin: 2rem 0 .6rem;
  border-left: 6px solid #FEBE01; font-size: 1.1rem;
}
.cta b {color: #FEBE01;}

/* footer: dark band */
.site-footer {
  text-align: center; color: #e9e3f0; font-size: .9rem; line-height: 1.7;
  background: linear-gradient(135deg, #1f4d2b, #3d1a5c);
  border-radius: 14px; margin-top: 3rem; padding: 1.4rem 1rem;
  border-top: 4px solid #FEBE01;
}
.site-footer b {color: #fff;}
.site-footer a {color: #FEBE01 !important;}
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
