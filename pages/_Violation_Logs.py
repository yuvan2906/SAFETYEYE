import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Violation Logs",
    page_icon="📋",
    layout="wide"
)

st.title("📋 SafetyEye Violation Logs")

csv_file = "alerts/alerts.csv"

if not os.path.exists(csv_file):
    st.warning("No violation logs found.")
    st.stop()

df = pd.read_csv(csv_file)

# ---------------------
# SEARCH
# ---------------------

search = st.text_input(
    "🔍 Search Alerts"
)

if search:
    df = df[
        df["Alert"]
        .astype(str)
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

# ---------------------
# FILTER
# ---------------------

filter_type = st.selectbox(
    "Filter",
    [
        "All",
        "Helmet",
        "Vest"
    ]
)

if filter_type == "Helmet":

    df = df[
        df["Alert"]
        .str.contains(
            "Helmet",
            case=False,
            na=False
        )
    ]

elif filter_type == "Vest":

    df = df[
        df["Alert"]
        .str.contains(
            "Vest",
            case=False,
            na=False
        )
    ]

# ---------------------
# KPI
# ---------------------

c1, c2 = st.columns(2)

c1.metric(
    "Total Records",
    len(df)
)

if len(df) > 0:
    c2.metric(
        "Latest Alert",
        df.iloc[-1]["Alert"]
    )

st.divider()

# ---------------------
# TABLE
# ---------------------

st.subheader("🚨 Alert Records")

st.dataframe(
    df.iloc[::-1],
    use_container_width=True
)

# ---------------------
# DOWNLOAD CSV
# ---------------------

csv_download = df.to_csv(
    index=False
)

st.download_button(
    label="⬇ Download CSV",
    data=csv_download,
    file_name="SafetyEye_Logs.csv",
    mime="text/csv"
)