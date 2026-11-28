"""
Free-estimate request form.
Emails each request to the business via SMTP using the [email] settings
in Streamlit Secrets. To change who receives requests, edit `recipient`
in Secrets — no code change needed.
"""
import smtplib
from email.message import EmailMessage
import streamlit as st
from site_config import BUSINESS, SERVICES

st.title("Request a Free Estimate")
st.write(f"Prefer to talk? Call **{BUSINESS['phone']}** · {BUSINESS['hours']}")


def send_email(data: dict) -> bool:
    try:
        if "email" not in st.secrets:
            return False
    except Exception:  # no secrets set at all
        return False
    cfg = st.secrets["email"]
    msg = EmailMessage()
    msg["Subject"] = f"New estimate request – {data['name']}"
    msg["From"] = cfg["sender"]
    msg["To"] = cfg["recipient"]
    msg["Reply-To"] = data["email"]
    msg.set_content("\n".join(f"{k.title()}: {v}" for k, v in data.items()))
    with smtplib.SMTP(cfg["smtp_server"], int(cfg.get("smtp_port", 587))) as s:
        s.starttls()
        s.login(cfg["sender"], cfg["password"])
        s.send_message(msg)
    return True


with st.form("estimate", clear_on_submit=True):
    c1, c2 = st.columns(2)
    name = c1.text_input("Name *")
    phone = c2.text_input("Phone *")
    email = c1.text_input("Email *")
    address = c2.text_input("Property address / city")
    services = st.multiselect("What do you need?", [s["title"] for s in SERVICES] + ["Other"])
    details = st.text_area("Tell us about the project")
    contact_pref = st.radio("Best way to reach you", ["Phone", "Text", "Email"],