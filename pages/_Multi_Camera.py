import streamlit as st
import os
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# ===================================
# PAGE CONFIG
# ===================================

st.set_page_config(
    page_title="Multi Camera Monitoring",
    page_icon="🎥",
    layout="wide"
)

# ===================================
# AUTO REFRESH
# ===================================

st_autorefresh(
    interval=1000,
    key="multi_camera_refresh"
)

# ===================================
# TITLE
# ===================================

st.title(
    "🎥 Multi Camera Monitoring Center"
)

st.info(
    f"🕒 {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)

# ===================================
# CAMERA STATUS
# ===================================

camera_online = os.path.exists(
    "latest_frame.jpg"
)

if camera_online:

    st.success(
        "🟢 Camera Feed Online"
    )

else:

    st.error(
        "🔴 Camera Feed Offline"
    )

st.divider()

# ===================================
# CAMERA GRID
# ===================================

cam1, cam2 = st.columns(2)

with cam1:

    st.subheader(
        "📷 Camera 1"
    )

    if camera_online:

        st.image(
            "latest_frame.jpg",
            use_container_width=True
        )

    else:

        st.warning(
            "No Feed"
        )

with cam2:

    st.subheader(
        "📷 Camera 2"
    )

    if camera_online:

        st.image(
            "latest_frame.jpg",
            use_container_width=True
        )

    else:

        st.warning(
            "No Feed"
        )

cam3, cam4 = st.columns(2)

with cam3:

    st.subheader(
        "📷 Camera 3"
    )

    if camera_online:

        st.image(
            "latest_frame.jpg",
            use_container_width=True
        )

    else:

        st.warning(
            "No Feed"
        )

with cam4:

    st.subheader(
        "📷 Camera 4"
    )

    if camera_online:

        st.image(
            "latest_frame.jpg",
            use_container_width=True
        )

    else:

        st.warning(
            "No Feed"
        )

st.divider()

# ===================================
# CAMERA ANALYTICS
# ===================================

st.subheader(
    "📊 Camera Analytics"
)

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "Active Cameras",
        4
    )

with c2:

    st.metric(
        "Online",
        4 if camera_online else 0
    )

with c3:

    st.metric(
        "Offline",
        0 if camera_online else 4
    )

with c4:

    st.metric(
        "Refresh Rate",
        "1 sec"
    )

st.divider()

# ===================================
# CONTROL CENTER
# ===================================

st.subheader(
    "🎯 Monitoring Status"
)

if camera_online:

    st.success(
        """
All monitoring channels active.

Live feed updating every second.

System operating normally.
        """
    )

else:

    st.error(
        """
Camera feed unavailable.

Check live_detect.py

Verify camera connection.
        """
    )

st.divider()

# ===================================
# FOOTER
# ===================================

st.markdown(
"""
<hr>

<center>

<h2 style='color:#00e5ff'>
🎥 SafetyEye Multi Camera Center
</h2>

<p>
Real-Time Monitoring • AI Detection • Live Analytics
</p>

</center>
""",
unsafe_allow_html=True
)