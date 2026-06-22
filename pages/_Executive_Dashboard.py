import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Executive Dashboard")
if os.path.exists("alerts/alerts.csv"):

    df = pd.read_csv(
        "alerts/alerts.csv"
    )

else:

    df = pd.DataFrame(
        columns=["Time","Alert"]
    )

total_violations = len(df)

safety_score = max(
    0,
    100 - (total_violations * 0.2)
)
k1,k2,k3 = st.columns(3)

with k1:

    st.metric(
        "🚨 Total Violations",
        total_violations
    )

with k2:

    st.metric(
        "🛡 Safety Score",
        round(
            safety_score,
            1
        )
    )

with k3:

    st.metric(
        "📅 Reports Generated",
        1
    )
st.subheader(
    "📈 Violation Summary"
)

if not df.empty:

    chart = px.histogram(
        df,
        x="Alert"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )
st.subheader(
    "🎯 Management Recommendation"
)

if safety_score > 90:

    st.success(
        """
Site performing well.

Continue monitoring.
        """
    )

elif safety_score > 70:

    st.warning(
        """
Improve PPE compliance.

Review violations.
        """
    )

else:

    st.error(
        """
Immediate action required.

Safety score critical.
        """
    )
st.subheader(
    "📋 Executive Summary"
)

st.info(
    f"""
Total Violations : {total_violations}

Safety Score : {round(safety_score,1)}

Current Status :
{"SAFE" if safety_score > 90 else "MONITOR"}
    """
)