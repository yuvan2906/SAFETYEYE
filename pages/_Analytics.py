import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="SafetyEye Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 SafetyEye Analytics")

csv_file = "alerts/alerts.csv"

if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
else:
    df = pd.DataFrame(columns=["Time", "Alert"])

if df.empty:
    st.warning("No analytics data available")
    st.stop()

# -------------------------
# COUNTS
# -------------------------

helmet_count = len(
    df[df["Alert"].str.contains("Helmet", na=False)]
)

vest_count = len(
    df[df["Alert"].str.contains("Vest", na=False)]
)

total = len(df)

compliance = max(
    0,
    min(
        100,
        100 - total
    )
)

# -------------------------
# KPI CARDS
# -------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("🚨 Total Violations", total)
c2.metric("⛑ Helmet Violations", helmet_count)
c3.metric("🦺 Vest Violations", vest_count)
c4.metric("🛡 Compliance %", f"{compliance}%")

st.divider()

# -------------------------
# PIE CHART
# -------------------------

left, right = st.columns(2)

with left:

    pie = px.pie(
        names=["Helmet", "Vest"],
        values=[helmet_count, vest_count],
        title="Violation Distribution"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

# -------------------------
# BAR CHART
# -------------------------

with right:

    bar = px.bar(
        x=["Helmet", "Vest"],
        y=[helmet_count, vest_count],
        title="Violation Comparison"
    )

    st.plotly_chart(
        bar,
        use_container_width=True
    )

st.divider()

# -------------------------
# TREND GRAPH
# -------------------------

try:

    df["Time"] = pd.to_datetime(df["Time"])

    trend = (
        df.groupby(
            df["Time"].dt.strftime("%H:%M")
        )
        .size()
        .reset_index(name="Count")
    )

    line = px.line(
        trend,
        x="Time",
        y="Count",
        title="Violation Trend"
    )

    st.plotly_chart(
        line,
        use_container_width=True
    )

except:
    st.warning("Trend unavailable")

st.divider()

# -------------------------
# RAW DATA
# -------------------------

st.subheader("📋 Analytics Data")

st.dataframe(
    df,
    use_container_width=True
)