import streamlit as st
import json
import os

st.set_page_config(
    page_title="Settings",
    page_icon="⚙",
    layout="wide"
)

st.title("⚙ SafetyEye Settings")

SETTINGS_FILE = "settings.json"

# ---------------------
# LOAD SETTINGS
# ---------------------

default_settings = {
    "confidence": 0.4,
    "cooldown": 5,
    "theme": "Dark",
    "auto_refresh": 2
}

if os.path.exists(SETTINGS_FILE):
    try:
        with open(SETTINGS_FILE, "r") as f:
            settings = json.load(f)
    except:
        settings = default_settings
else:
    settings = default_settings

# ---------------------
# DETECTION SETTINGS
# ---------------------

st.subheader("🎯 Detection Settings")

confidence = st.slider(
    "Confidence Threshold",
    0.1,
    1.0,
    float(settings.get("confidence", 0.4)),
    0.05
)

cooldown = st.slider(
    "Alert Cooldown (seconds)",
    1,
    30,
    int(settings.get("cooldown", 5))
)

# ---------------------
# DASHBOARD SETTINGS
# ---------------------

st.subheader("🖥 Dashboard Settings")

theme = st.selectbox(
    "Theme",
    ["Dark"]
)

auto_refresh = st.slider(
    "Auto Refresh Interval",
    1,
    10,
    int(settings.get("auto_refresh", 2))
)

# ---------------------
# SAVE BUTTON
# ---------------------

if st.button("💾 Save Settings"):

    data = {
        "confidence": confidence,
        "cooldown": cooldown,
        "theme": theme,
        "auto_refresh": auto_refresh
    }

    with open(
        SETTINGS_FILE,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )

    st.success("Settings Saved Successfully!")

# ---------------------
# CURRENT SETTINGS
# ---------------------

st.subheader("📋 Current Settings")

st.json({
    "confidence": confidence,
    "cooldown": cooldown,
    "theme": theme,
    "auto_refresh": auto_refresh
})