import streamlit as st
import glob
import os

st.set_page_config(
    page_title="Screenshot Gallery",
    page_icon="📸",
    layout="wide"
)

st.title("📸 Violation Evidence Gallery")

images = sorted(
    glob.glob(
        "alerts/screenshots/*.jpg"
    ),
    reverse=True
)

if len(images) == 0:

    st.warning(
        "No screenshots available."
    )

else:

    cols = st.columns(3)

    for i, img in enumerate(images):

        cols[i % 3].image(
            img,
            caption=os.path.basename(img),
            use_container_width=True
        )