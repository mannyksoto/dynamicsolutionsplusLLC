from pathlib import Path
import streamlit as st

st.title("Our Work")
st.write("A few recent projects.")

# Drop the customer's job photos (.jpg / .png) into assets/gallery/
# Name them like "front-yard-install.jpg" — the file name becomes the caption.
gallery_dir = Path(__file__).parent.parent / "assets" / "gallery"
photos = sorted(
    p for p in gallery_dir.glob("*") if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
) if gallery_dir.exists() else []

if not photos:
    st.info("Project photos coming soon! (Add images to `assets/gallery/` to fill this page.)")
else:
    cols = st.columns(3)
    for i, photo in enumerate(photos):
        caption = photo.stem.replace("-", " ").replace("_", " ").title()
        cols[i % 3].image(str(photo), caption=caption, width="stretch")
