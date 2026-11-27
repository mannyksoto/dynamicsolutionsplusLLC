import streamlit as st
from site_config import SERVICES
from ui import call_to_action

st.title("Our Services")
st.write("From a brand-new landscape to a sprinkler head that won't pop up — we've got you covered.")

for i in range(0, len(SERVICES), 2):
    cols = st.columns(2)
    for col, svc in zip(cols, SERVICES[i:i + 2]):
        items = "".join(f"<li>{d}</li>" for d in svc["details"])
        col.markdown(
            f"""<div class="card"><div class="icon">{svc['icon']}</div>
            <h3>{svc['title']}</h3><p>{svc['blurb']}</p><ul>{items}</ul></div>""",
            unsafe_allow_html=True,
        )
    st.write("")

call_to_action()
