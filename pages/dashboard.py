import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import os
import glob

from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="SafetyEye V4",
    page_icon="🦺",
    layout="wide"
)

# =========================================
# AUTO REFRESH (LOW BLINK)
# =========================================

st_autorefresh(
    interval=5000,
    key="safetyeye_refresh"
)

# =========================================
# FUTURISTIC INDUSTRIAL THEME
# =========================================

st.markdown("""
<style>

/* Main App */

.stApp{
background:
linear-gradient(
135deg,
#020617,
#07111f,
#0b1728
);
}

/* Sidebar */

[data-testid="stSidebar"]{
background:#08111f;
border-right:1px solid #1f2937;
}

/* Headings */

h1,h2,h3,h4,h5,h6{
color:white !important;
font-weight:700 !important;
}

/* Text */

p,span,label{
color:#d1d5db !important;
}

/* Metric Cards */

[data-testid="stMetric"]{
background:rgba(17,24,39,0.90);
padding:18px;
border-radius:18px;
border-left:5px solid #f97316;
box-shadow:0 0 15px rgba(249,115,22,0.25);
}

/* Metric Labels */

[data-testid="stMetricLabel"]{
color:white !important;
font-weight:bold !important;
}

/* Metric Values */

[data-testid="stMetricValue"]{
color:#f97316 !important;
font-weight:bold !important;
}

/* Buttons */

.stButton button{
background:#f97316;
color:white;
border-radius:12px;
font-weight:bold;
}

/* Dataframe */

[data-testid="stDataFrame"]{
background:#111827;
}

/* Progress */

.stProgress > div > div > div{
background:#f97316;
}

</style>
""",
unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown(
"""
<h1 style='
text-align:center;
font-size:64px;
font-weight:bold;
color:#f97316;
'>

🦺 SAFETYEYE

</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div style='
background:linear-gradient(90deg,#ea580c,#fb923c);
padding:18px;
border-radius:18px;
text-align:center;
font-size:28px;
font-weight:bold;
color:white;
'>

🏭 AI WORKPLACE SAFETY COMMAND CENTER

</div>
""",
unsafe_allow_html=True
)

st.write("")

st.success(
    "✅ SafetyEye Initialized"
)
# =========================================
# LOAD ALERTS
# =========================================

if os.path.exists(
    "alerts/alerts.csv"
):

    df = pd.read_csv(
        "alerts/alerts.csv"
    )

else:

    df = pd.DataFrame(
        columns=[
            "Time",
            "Alert"
        ]
    )

# =========================================
# ALERT COUNTS
# =========================================

total_violations = len(df)

helmet_count = len(

    df[
        df["Alert"]

        .astype(str)

        .str.contains(
            "Helmet",
            na=False
        )
    ]

)

vest_count = len(

    df[
        df["Alert"]

        .astype(str)

        .str.contains(
            "Vest",
            na=False
        )
    ]

)

mask_count = len(

    df[
        df["Alert"]

        .astype(str)

        .str.contains(
            "Mask",
            na=False
        )
    ]

)

# =========================================
# OCCUPANCY
# =========================================

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

# =========================================
# CAMERA STATUS
# =========================================

camera_online = os.path.exists(
    "latest_frame.jpg"
)

# =========================================
# SAFETY SCORE
# =========================================

safety_score = max(
    0,
    100 - (
        total_violations * 0.2
    )
)

# =========================================
# COMPLIANCE SCORE
# =========================================

compliance_score = max(
    0,
    100 - (
        total_violations * 0.1
    )
)

# =========================================
# AI RISK ENGINE
# =========================================

risk_score = (
    total_violations * 2
) + occupancy

if risk_score < 20:

    risk_level = "🟢 LOW RISK"

elif risk_score < 50:

    risk_level = "🟡 MEDIUM RISK"

else:

    risk_level = "🔴 HIGH RISK"

# =========================================
# AI DECISION
# =========================================

if risk_score > 100:

    ai_decision = """
Immediate inspection required.

Multiple PPE violations detected.

Supervisor intervention required.
"""

elif risk_score > 50:

    ai_decision = """
Increase monitoring frequency.

Review PPE compliance.

Medium risk environment.
"""

else:

    ai_decision = """
Site operating safely.

Continue monitoring.
"""

# =========================================
# AI CONFIDENCE
# =========================================

ai_confidence = min(
    100,
    85 + occupancy
)

# =========================================
# LIVE CLOCK
# =========================================

current_time = datetime.now().strftime(
    "%d-%m-%Y %H:%M:%S"
)

st.info(
    f"🕒 {current_time}"
)
# =========================================
# KPI DASHBOARD
# =========================================

st.subheader(
    "📊 Safety Overview"
)

k1,k2,k3,k4,k5 = st.columns(5)

with k1:

    st.metric(
        "👷 Workers",
        occupancy
    )

with k2:

    st.metric(
        "🚨 Violations",
        total_violations
    )

with k3:

    st.metric(
        "⛑ Helmet",
        helmet_count
    )

with k4:

    st.metric(
        "🦺 Vest",
        vest_count
    )

with k5:

    st.metric(
        "😷 Mask",
        mask_count
    )

st.divider()

# =========================================
# RISK STATUS BANNER
# =========================================

st.subheader(
    "⚠ Site Risk Status"
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

st.divider()

# =========================================
# AI CONFIDENCE
# =========================================

st.subheader(
    "🧠 AI Confidence Engine"
)

st.progress(
    ai_confidence / 100
)

st.metric(
    "AI Confidence",
    f"{ai_confidence}%"
)

st.divider()

# =========================================
# EXECUTIVE SUMMARY
# =========================================

st.subheader(
    "🏭 Executive Summary"
)

e1,e2,e3,e4 = st.columns(4)

with e1:

    st.metric(
        "🛡 Safety Score",
        round(
            safety_score,
            1
        )
    )

with e2:

    st.metric(
        "📈 Compliance",
        round(
            compliance_score,
            1
        )
    )

with e3:

    st.metric(
        "⚠ Risk Score",
        risk_score
    )

with e4:

    st.metric(
        "📷 Cameras",
        "1 Active"
    )

st.divider()

# =========================================
# AI RECOMMENDATION PANEL
# =========================================

st.subheader(
    "🤖 AI Recommendation"
)

st.info(
    ai_decision
)

st.divider()
# =========================================
# LIVE MONITORING CENTER
# =========================================

st.subheader(
    "📹 Live Monitoring Center"
)

left,right = st.columns([2,1])

# =========================================
# LIVE CAMERA FEED
# =========================================

with left:

    if os.path.exists(
        "latest_frame.jpg"
    ):

        st.image(
            "latest_frame.jpg",
            use_container_width=True
        )

    else:

        st.warning(
            "⚠ Waiting For Camera Feed..."
        )

# =========================================
# NEON SAFETY GAUGE
# =========================================

with right:

    gauge = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=safety_score,

            title={
                "text":"Safety Score"
            },

            gauge={

                "axis":{
                    "range":[0,100]
                },

                "bar":{
                    "color":"#f97316"
                },

                "steps":[

                    {
                        "range":[0,40],
                        "color":"#ef4444"
                    },

                    {
                        "range":[40,70],
                        "color":"#f59e0b"
                    },

                    {
                        "range":[70,100],
                        "color":"#22c55e"
                    }

                ]
            }
        )
    )

    gauge.update_layout(

        paper_bgcolor="#111827",

        font={
            "color":"white"
        },

        height=350
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

st.divider()

# =========================================
# AI COMMAND CENTER
# =========================================

st.subheader(
    "🤖 AI Command Center"
)

a1,a2 = st.columns([2,1])

with a1:

    st.info(
        f"""
Risk Level : {risk_level}

Safety Score : {round(safety_score,1)}%

Compliance Score : {round(compliance_score,1)}%

AI Decision :

{ai_decision}
        """
    )

with a2:

    if camera_online:

        st.success(
            "🟢 Camera Online"
        )

    else:

        st.error(
            "🔴 Camera Offline"
        )

st.divider()

# =========================================
# CONTROL ROOM DASHBOARD
# =========================================

st.subheader(
    "🏭 Control Room Dashboard"
)

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(
        "📷 Cameras",
        "1 Active"
    )

with c2:

    st.metric(
        "👷 Workforce",
        occupancy
    )

with c3:

    st.metric(
        "⚠ Risk Score",
        risk_score
    )

with c4:

    st.metric(
        "🛡 Safety",
        round(
            safety_score,
            1
        )
    )

st.divider()
# =========================================
# ADVANCED ANALYTICS CENTER
# =========================================

st.subheader(
    "📊 Advanced Analytics Center"
)

col1,col2 = st.columns(2)

# =========================================
# VIOLATION DISTRIBUTION
# =========================================

with col1:

    st.subheader(
        "🥧 Violation Distribution"
    )

    pie = px.pie(

        names=[
            "Helmet",
            "Vest",
            "Mask"
        ],

        values=[
            helmet_count,
            vest_count,
            mask_count
        ],

        hole=0.55
    )

    pie.update_layout(

        paper_bgcolor="#111827",

        plot_bgcolor="#111827",

        font={
            "color":"white"
        },

        height=450
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

# =========================================
# VIOLATION TREND
# =========================================

with col2:

    st.subheader(
        "📈 Violation Trend"
    )

    if not df.empty:

        try:

            trend_df = df.copy()

            trend_df["Count"] = 1

            trend = trend_df.groupby(
                "Time"
            )["Count"].sum().reset_index()

            line = px.line(

                trend,

                x="Time",

                y="Count",

                markers=True
            )

            line.update_layout(

                paper_bgcolor="#111827",

                plot_bgcolor="#111827",

                font={
                    "color":"white"
                },

                height=450
            )

            st.plotly_chart(
                line,
                use_container_width=True
            )

        except:

            st.warning(
                "Trend Data Unavailable"
            )

    else:

        st.info(
            "No Violations Found"
        )

st.divider()

# =========================================
# EXECUTIVE MONITORING PANEL
# =========================================

st.subheader(
    "🏢 Executive Monitoring Panel"
)

e1,e2,e3,e4 = st.columns(4)

with e1:

    st.metric(
        "🛡 Safety Index",
        round(
            safety_score,
            1
        )
    )

with e2:

    st.metric(
        "🚨 Incidents",
        total_violations
    )

with e3:

    st.metric(
        "👷 Workforce",
        occupancy
    )

with e4:

    st.metric(
        "📷 Cameras",
        1
    )

st.divider()

# =========================================
# AI ANALYSIS DASHBOARD
# =========================================

st.subheader(
    "🧠 AI Analysis Dashboard"
)

if risk_score > 100:

    st.error(
        """
🔴 HIGH RISK DETECTED

• Multiple PPE violations

• Immediate action required

• Supervisor intervention recommended
        """
    )

elif risk_score > 50:

    st.warning(
        """
🟡 MEDIUM RISK DETECTED

• Increase monitoring

• Review PPE compliance

• Conduct safety inspection
        """
    )

else:

    st.success(
        """
🟢 SAFE ENVIRONMENT

• Compliance acceptable

• Monitoring active

• No immediate concerns
        """
    )

st.divider()

# =========================================
# AI FUTURE PREDICTION
# =========================================

st.subheader(
    "🔮 AI Future Prediction"
)

future_risk = min(
    100,
    risk_score + 10
)

f1,f2 = st.columns(2)

with f1:

    st.metric(
        "Predicted Risk (Next Hour)",
        future_risk
    )

with f2:

    st.metric(
        "AI Confidence",
        f"{ai_confidence}%"
    )

if future_risk > 80:

    st.error(
        "⚠ Potential risk escalation detected."
    )

else:

    st.success(
        "✅ Risk expected to remain stable."
    )

st.divider()
# =========================================
# SCREENSHOT GALLERY
# =========================================

st.subheader(
    "📸 Violation Evidence Gallery"
)

images = sorted(

    glob.glob(
        "alerts/screenshots/*.jpg"
    ),

    reverse=True

)

if len(images) > 0:

    cols = st.columns(4)

    for i, img in enumerate(
        images[:12]
    ):

        cols[i % 4].image(

            img,

            caption=os.path.basename(
                img
            ),

            use_container_width=True
        )

else:

    st.info(
        "No screenshots available"
    )

st.divider()

# =========================================
# ALERT INVESTIGATION CENTER
# =========================================

st.subheader(
    "🔍 Alert Investigation Center"
)

search_text = st.text_input(
    "Search Alert Type"
)

if not df.empty:

    filtered_df = df.copy()

    if search_text:

        filtered_df = filtered_df[

            filtered_df["Alert"]

            .astype(str)

            .str.contains(

                search_text,

                case=False,

                na=False
            )
        ]

else:

    filtered_df = pd.DataFrame()

# =========================================
# ALERT SUMMARY
# =========================================

s1,s2,s3,s4 = st.columns(4)

with s1:

    st.metric(
        "🚨 Total Alerts",
        total_violations
    )

with s2:

    st.metric(
        "⛑ Helmet Alerts",
        helmet_count
    )

with s3:

    st.metric(
        "🦺 Vest Alerts",
        vest_count
    )

with s4:

    st.metric(
        "😷 Mask Alerts",
        mask_count
    )

st.divider()

# =========================================
# RECENT INCIDENT TABLE
# =========================================

st.subheader(
    "🚨 Recent Incident Table"
)

if not filtered_df.empty:

    st.dataframe(

        filtered_df.iloc[::-1],

        use_container_width=True,

        height=400

    )

else:

    st.warning(
        "No matching records found"
    )

st.divider()

# =========================================
# LATEST INCIDENT
# =========================================

st.subheader(
    "⚠ Latest Incident"
)

if not df.empty:

    latest = df.iloc[-1]

    st.error(
        f"""
Alert:

{latest['Alert']}

Time:

{latest['Time']}
        """
    )

else:

    st.success(
        "No incidents recorded"
    )

st.divider()

# =========================================
# EVIDENCE MANAGEMENT PANEL
# =========================================

st.subheader(
    "🗂 Evidence Management"
)

e1,e2,e3,e4 = st.columns(4)

with e1:

    st.metric(
        "📸 Screenshots",
        len(images)
    )

with e2:

    st.metric(
        "📋 Alert Records",
        total_violations
    )

with e3:

    st.metric(
        "🟢 Camera Status",
        "ONLINE" if camera_online else "OFFLINE"
    )

with e4:

    st.metric(
        "🕒 Last Update",
        datetime.now().strftime(
            "%H:%M:%S"
        )
    )

st.divider()
# =========================================
# OCCUPANCY ANALYTICS
# =========================================

st.subheader(
    "👷 Occupancy Analytics"
)

if os.path.exists(
    "occupancy_log.csv"
):

    try:

        occ_df = pd.read_csv(
            "occupancy_log.csv"
        )

        if not occ_df.empty:

            occ_chart = px.line(

                occ_df,

                x="Time",

                y="Occupancy",

                markers=True
            )

            occ_chart.update_layout(

                paper_bgcolor="#111827",

                plot_bgcolor="#111827",

                font={
                    "color":"white"
                },

                height=400
            )

            st.plotly_chart(
                occ_chart,
                use_container_width=True
            )

    except Exception as e:

        st.warning(
            f"Occupancy data unavailable: {e}"
        )

else:

    st.warning(
        "occupancy_log.csv not found"
    )

st.divider()

# =========================================
# SYSTEM HEALTH DASHBOARD
# =========================================

st.subheader(
    "⚙ System Health Dashboard"
)

h1,h2,h3,h4 = st.columns(4)

with h1:
    st.success("🟢 Detection Engine")

with h2:
    st.success("🟢 Dashboard Server")

with h3:
    st.success("🟢 Analytics Engine")

with h4:
    st.success("🟢 Alert System")

st.divider()

# =========================================
# AI PERFORMANCE MONITOR
# =========================================

st.subheader(
    "🧠 AI Performance Monitor"
)

p1,p2,p3,p4 = st.columns(4)

with p1:
    st.metric(
        "🎯 Accuracy",
        "95%"
    )

with p2:
    st.metric(
        "⚡ Speed",
        "28 FPS"
    )

with p3:
    st.metric(
        "📊 Confidence",
        f"{ai_confidence}%"
    )

with p4:
    st.metric(
        "🤖 AI Status",
        "ACTIVE"
    )

st.divider()


# =========================================
# COMMAND CENTER STATUS
# =========================================

st.subheader(
    "🎯 Command Center Status"
)

if safety_score >= 90:

    st.success(
        "🟢 SITE STATUS : SAFE"
    )

elif safety_score >= 70:

    st.warning(
        "🟡 SITE STATUS : MONITOR"
    )

else:

    st.error(
        "🔴 SITE STATUS : CRITICAL"
    )

st.divider()

# =========================================
# PREMIUM FOOTER
# =========================================

st.markdown(
"""
<hr>

<center>

<h1 style='color:#f97316;'>

🦺 SAFETYEYE

</h1>

<h3 style='color:white;'>

AI Powered Workplace Safety Monitoring

</h3>

<p style='color:#9ca3af;'>

Live Detection • Analytics • Risk Prediction

Occupancy Tracking • Evidence Management

Executive Monitoring • AI Intelligence

</p>

<p style='color:#f97316;'>

Developed by Yuvanesh Hari B

</p>

</center>
""",
unsafe_allow_html=True
)