"""
Free-estimate request form.
Emails each request to the business via SMTP using the [email] settings
in Streamlit Secrets. To change who receives requests, edit `recipient`
in Secrets — no code change needed.
"""
import re
import smtplib
from email.message import EmailMessage
import streamlit as st
from site_config import BUSINESS, SERVICES

US_STATES = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL",
    "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE",
    "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD",
    "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
]

# ---------- validation rules ----------
NAME_RE = re.compile(r"^[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ .'\-]*[A-Za-zÀ-ÿ.]$")
EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}$")
STREET_RE = re.compile(r"^\d+[A-Za-z]?\s+[A-Za-z0-9 .'#\-]{2,}$")
CITY_RE = re.compile(r"^[A-Za-z][A-Za-z .'\-]*[A-Za-z.]$")
ZIP_RE = re.compile(r"^\d{5}(-\d{4})?$")


def format_phone(raw: str):
    """Return '(573) 216-4436' if raw has a full 10-digit US number, else None."""
    digits = re.sub(r"\D", "", raw)
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    if len(digits) != 10 or digits[0] in "01" or digits[3] in "01":
        return None
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"


def validate(f: dict) -> dict:
    """Return {field: error message} for every problem found."""
    errors = {}
    name = f["name"].strip()
    if not name:
        errors["name"] = "Please enter your name."
    elif not NAME_RE.match(name) or len(name.split()) < 2:
        errors["name"] = "Please enter your first and last name (letters only, no numbers)."

    if not f["phone"].strip():
        errors["phone"] = "Please enter your phone number."
    elif not format_phone(f["phone"]):
        errors["phone"] = "Please enter a full 10-digit phone number with area code, e.g. (573) 555-1234."

    if not f["email"].strip():
        errors["email"] = "Please enter your email."
    elif not EMAIL_RE.match(f["email"].strip()):
        errors["email"] = "Please enter a valid email, e.g. name@example.com."

    if not f["street"].strip():
        errors["street"] = "Please enter the street address."
    elif not STREET_RE.match(f["street"].strip()):
        errors["street"] = "Please enter a street address starting with the house number, e.g. 123 Main St."

    if not f["city"].strip():
        errors["city"] = "Please enter the city."
    elif not CITY_RE.match(f["city"].strip()):
        errors["city"] = "City should contain letters only."

    if not f["state"]:
        errors["state"] = "Please choose a state."

    if not f["zip"].strip():
        errors["zip"] = "Please enter the ZIP code."
    elif not ZIP_RE.match(f["zip"].strip()):
        errors["zip"] = "Please enter a 5-digit ZIP code, e.g. 63301."

    if not f["services"]:
        errors["services"] = "Please choose at least one service."
    return errors


# ---------- email ----------
def send_email(data: dict) -> bool:
    try:
        if "email" not in st.secrets:
            return False
    except Exception:  # no secrets set at all
        return False
    cfg = st.secrets["email"]
    msg = EmailMessage()
    msg["Subject"] = f"New estimate request – {data['Name']}"
    msg["From"] = cfg["sender"]
    msg["To"] = cfg["recipient"]
    msg["Reply-To"] = data["Email"]
    msg.set_content("\n".join(f"{k}: {v}" for k, v in data.items()))
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


# ---------- page ----------
st.title("Request a Free Estimate")
st.write(f"Prefer to talk? Call **{BUSINESS['phone']}** · {BUSINESS['hours']}")

# n changes after a successful send so the visitor gets a fresh, empty form.
st.session_state.setdefault("form_n", 0)
n = st.session_state.form_n
if st.session_state.pop("just_sent", None) is not None:
    st.success("Thanks! We got your request and will be in touch within 1 business day.")

# Red outline on every field that has a problem
errors = st.session_state.get("form_errors", {})
if errors:
    selectors = ", ".join(f".st-key-{f}_{n} div:has(> input)" for f in errors)
    st.markdown(
        f"""<style>
        {selectors} {{border-color: #d93025 !important; box-shadow: 0 0 0 1px #d93025 !important;}}
        .field-err {{color: #d93025; font-size: .85rem; margin: -.6rem 0 .6rem;}}
        </style>""",
        unsafe_allow_html=True,
    )


def check_form():
    """Runs when Send Request is pressed, before the page redraws."""
    ss = st.session_state
    fields = {f: ss.get(f"{f}_{n}") or "" for f in
              ["name", "phone", "email", "street", "city", "state", "zip"]}
    fields["services"] = ss.get(f"services_{n}") or []
    ss.form_errors = validate(fields)
    ss.do_send = not ss.form_errors


def field_error(container, field):
    """Show the short error message under a field, if it has one."""
    if field in errors:
        container.markdown(f'<div class="field-err">{errors[field]}</div>', unsafe_allow_html=True)


with st.form(f"estimate_{n}"):
    c1, c2 = st.columns(2)
    name = c1.text_input("Full name *", placeholder="Jane Smith", key=f"name_{n}")
    field_error(c1, "name")
    phone = c2.text_input("Phone *", placeholder="(573) 555-1234", key=f"phone_{n}")
    field_error(c2, "phone")
    email = st.text_input("Email *", placeholder="name@example.com", key=f"email_{n}")
    field_error(st, "email")

    st.markdown("**Property address**")
    a1, a2 = st.columns([3, 1])
    street = a1.text_input("Street address *", placeholder="123 Main St", key=f"street_{n}")
    field_error(a1, "street")
    suite = a2.text_input("Apt / Suite (optional)", key=f"suite_{n}")
    b1, b2, b3 = st.columns([3, 1, 1.4])
    city = b1.text_input("City *", placeholder="St. Charles", key=f"city_{n}")
    field_error(b1, "city")
    state = b2.selectbox("State *", US_STATES, index=US_STATES.index("MO"), key=f"state_{n}")
    zip_code = b3.text_input("ZIP *", placeholder="63301", max_chars=10, key=f"zip_{n}")
    field_error(b3, "zip")

    services = st.pills(
        "What do you need? (Choose at least one) *",
        [s["title"] for s in SERVICES] + ["Other"],
        selection_mode="multi",
        key=f"services_{n}",
    )
    field_error(st, "services")
    details = st.text_area("Tell us about the project", key=f"details_{n}")
    contact_pref = st.radio("Best way to reach you", ["Phone", "Text", "Email"],
                            horizontal=True, key=f"pref_{n}")
    st.form_submit_button("Send Request", type="primary", on_click=check_form)

if errors:
    st.error("Please fix the error shown above." if len(errors) == 1
             else "Please fix the errors shown above.")

if st.session_state.pop("do_send", False):
    address = street.strip() + (f", {suite.strip()}" if suite.strip() else "")
    address += f", {city.strip()}, {state} {zip_code.strip()}"
    data = {
        "Name": name.strip(),
        "Phone": format_phone(phone),
        "Email": email.strip(),
        "Address": address,
        "Services": ", ".join(services),
        "Best way to reach": contact_pref,
        "Details": details.strip() or "(none)",
    }
    try:
        sent = send_email(data)
    except Exception as e:
        print(f"Estimate email failed: {e!r}")
        st.error(f"Something went wrong sending your request. Please call {BUSINESS['phone']}.")
    else:
        if sent:
            st.session_state.form_n += 1      # fresh empty form
            st.session_state.just_sent = True
            st.rerun()
        else:
            st.success("Thanks! We got your request and will be in touch within 1 business day.")
            st.caption("⚠️ Dev note: email secrets not configured — request was not delivered.")