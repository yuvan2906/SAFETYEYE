import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go

# ===================================
# PAGE TITLE
# ===================================

st.title("🤖 AI Risk Prediction")

# ===================================
# LOAD ALERTS
# ===================================

if os.path.exists("alerts/alerts.csv"):

    df = pd.read_csv(
        "alerts/alerts.csv"
    )

    violations = len(df)

else:

    violations = 0

# ===================================
# LOAD OCCUPANCY
# ===================================

occupancy = 0

if os.path.exists(
    "occupancy.txt"
):

    try:

        with open(
            "occupancy.txt",
            "r"
        ) as f:

            occupancy = int(
                f.read()
            )

    except:

        occupancy = 0

# ===================================
# SAFETY SCORE
# ===================================

safety_score = max(
    0,
    100 - (
        violations * 0.2
    )
)

# ===================================
# AI RISK ENGINE
# ===================================

risk_score = (
    violations * 2
) + (
    occupancy
)

if risk_score < 20:

    risk = "🟢 LOW RISK"

    color = "green"

elif risk_score < 50:

    risk = "🟡 MEDIUM RISK"

    color = "orange"

else:

    risk = "🔴 HIGH RISK"

    color = "red"

# ===================================
# METRICS
# ===================================

m1,m2 = st.columns(2)

with m1:

    st.metric(
        "🛡 Safety Score",
        round(
            safety_score,
            2
        )
    )

with m2:

    st.metric(
        "⚠ Risk Score",
        risk_score
    )

# ===================================
# RISK STATUS
# ===================================

st.markdown(
    f"""
    <h1 style='color:{color}'>
    {risk}
    </h1>
    """,
    unsafe_allow_html=True
)

# ===================================
# RISK METER
# ===================================

st.subheader(
    "⚠ Risk Meter"
)

st.progress(
    min(
        risk_score,
        100
    ) / 100
)

# ===================================
# RISK GAUGE
# ===================================

fig = go.Figure()

fig.add_trace(

    go.Indicator(

        mode="gauge+number",

        value=risk_score,

        title={
            "text":"Risk Level"
        },

        gauge={

            "axis":{
                "range":[0,200]
            },

            "bar":{
                "color":"red"
            },

            "steps":[

                {
                    "range":[0,50],
                    "color":"green"
                },

                {
                    "range":[50,100],
                    "color":"orange"
                },

                {
                    "range":[100,200],
                    "color":"red"
                }
            ]
        }
    )
)

fig.update_layout(
    height=400
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ===================================
# AI RECOMMENDATION
# ===================================

st.subheader(
    "🤖 AI Recommendation"
)

if risk_score > 100:

    st.error(
        """
Immediate inspection required.

Multiple PPE violations detected.

Enforce PPE compliance immediately.
        """
    )

elif risk_score > 50:

    st.warning(
        """
Medium Risk Environment.

Increase monitoring.

Review worker safety procedures.
        """
    )

else:

    st.success(
        """
Site Operating Safely.

Continue monitoring.

Maintain PPE compliance.
        """
    )

# ===================================
# PREDICTION FACTORS
# ===================================

st.subheader(
    "📊 Prediction Factors"
)

p1,p2 = st.columns(2)

with p1:

    st.info(
        f"👷 Occupancy : {occupancy}"
    )

with p2:

    st.info(
        f"🚨 Violations : {violations}"
    )

# ===================================
# AI CONFIDENCE
# ===================================

st.subheader(
    "🧠 AI Confidence"
)

ai_confidence = min(
    100,
    85 + occupancy
)

st.progress(
    ai_confidence / 100
)

st.write(
    f"AI Confidence : {ai_confidence}%"
)

# ===================================
# FINAL DECISION
# ===================================

st.subheader(
    "🎯 Final Decision"
)

if risk_score > 100:

    st.error(
        "🔴 HIGH RISK SITE"
    )

elif risk_score > 50:

    st.warning(
        "🟡 MEDIUM RISK SITE"
    )

else:

    st.success(
        "🟢 SAFE SITE"
    )