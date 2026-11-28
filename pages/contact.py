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
    port = int(cfg.get("smtp_port", 465))
    if port == 465:
        server = smtplib.SMTP_SSL(cfg["smtp_server"], port, timeout=20)
    else:
        server = smtplib.SMTP(cfg["smtp_server"], port, timeout=20)
        server.starttls()
    with server as s:
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
    contact_pref = st.radio("Best way to reach you", ["Phone", "Text", "Email"], horizontal=True)
    submitted = st.form_submit_button("Send Request", type="primary")



if submitted:
    if not (name and phone and email):
        st.error("Please fill in your name, phone and email.")
    else:
        data = {
            "name": name, "phone": phone, "email": email, "address": address,
            "services": ", ".join(services) or "Not specified",
            "contact preference": contact_pref, "details": details,
        }
        try:
            sent = send_email(data)
        except Exception as e:
            print(f"Estimate email failed: {e!r}")
            sent = False
            st.error(f"Something went wrong sending your request. Please call {BUSINESS['phone']}.")
            st.code(repr(e))  # TEMP: remove after testing
        else:
            st.success("Thanks! We got your request and will be in touch within 1 business day.")
            if not sent:
                st.caption("⚠️ Dev note: email secrets not configured — request was not delivered.")
