import streamlit as st
import os
import glob
from PIL import Image
from streamlit_autorefresh import st_autorefresh

# Auto Refresh Every 2 Seconds
st_autorefresh(interval=2000, key="live_refresh")

st.set_page_config(
    page_title="Live Monitoring",
    page_icon="📹",
    layout="wide"
)

st.title("📹 SafetyEye Live Monitoring")

# -------------------
# STATUS CARDS
# -------------------

occupancy = 0

if os.path.exists("occupancy.txt"):
    try:
        with open("occupancy.txt", "r") as f:
            occupancy = int(f.read())
    except:
        occupancy = 0

c1, c2, c3 = st.columns(3)

c1.metric("👷 Occupancy", occupancy)

if os.path.exists("latest_frame.jpg"):
    c2.success("🟢 Camera Online")
else:
    c2.error("🔴 Camera Offline")

screenshots = glob.glob(
    "alerts/screenshots/*.jpg"
)

c3.metric(
    "📸 Evidence Images",
    len(screenshots)
)

st.divider()

# -------------------
# LIVE FEED
# -------------------

st.subheader("📹 Live Camera Feed")

if os.path.exists("latest_frame.jpg"):

    image = Image.open(
        "latest_frame.jpg"
    )

    st.image(
        image,
        use_container_width=True
    )

else:

    st.warning(
        "Waiting for Camera Feed..."
    )

st.divider()

# -------------------
# EVIDENCE GALLERY
# -------------------

st.subheader(
    "📸 Recent Violation Screenshots"
)

images = sorted(
    glob.glob(
        "alerts/screenshots/*.jpg"
    ),
    reverse=True
)

if len(images) > 0:

    cols = st.columns(3)

    for i, img in enumerate(images[:9]):

        cols[i % 3].image(
            img,
            use_container_width=True
        )

else:

    st.info(
        "No screenshots captured yet."
    )

st.divider()

# -------------------
# SYSTEM STATUS
# -------------------

st.subheader("⚙ System Status")

if os.path.exists("latest_frame.jpg"):
    st.success(
        "Detection System Running"
    )
else:
    st.error(
        "Detection System Offline"
    )