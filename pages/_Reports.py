import streamlit as st
import pandas as pd
import os
import subprocess

st.set_page_config(
    page_title="Safety Reports",
    page_icon="📄",
    layout="wide"
)

st.title("📄 SafetyEye Reports")

# ===================================
# ALERT DATA
# ===================================

alert_file = "alerts/alerts.csv"

if os.path.exists(alert_file):

    df = pd.read_csv(alert_file)

else:

    df = pd.DataFrame(
        columns=["Time", "Alert"]
    )

# ===================================
# OCCUPANCY
# ===================================

occupancy = 0

if os.path.exists("occupancy.txt"):

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

total_violations = len(df)

safety_score = max(
    0,
    100 - (total_violations * 0.2)
)

# ===================================
# METRICS
# ===================================

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "🚨 Violations",
        total_violations
    )

with c2:

    st.metric(
        "👷 Occupancy",
        occupancy
    )

with c3:

    st.metric(
        "🛡 Safety Score",
        round(safety_score, 1)
    )

st.divider()

# ===================================
# GENERATE REPORT
# ===================================

st.subheader(
    "📄 Generate Report"
)

if st.button(
    "📄 Generate New Report"
):

    try:

        subprocess.run(
            ["python", "pdf_report.py"]
        )

        st.success(
            "✅ Report Generated Successfully"
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

st.divider()

# ===================================
# DOWNLOAD REPORT
# ===================================

st.subheader(
    "📥 Download Report"
)

if os.path.exists(
    "SafetyEye_Report.pdf"
):

    with open(
        "SafetyEye_Report.pdf",
        "rb"
    ) as f:

        st.download_button(
            label="⬇ Download PDF Report",
            data=f,
            file_name="SafetyEye_Report.pdf",
            mime="application/pdf"
        )

else:

    st.warning(
        "No PDF report found. Generate one first."
    )

st.divider()

# ===================================
# RECENT VIOLATIONS
# ===================================

st.subheader(
    "🚨 Recent Violations"
)

if not df.empty:

    st.dataframe(
        df.tail(20),
        use_container_width=True
    )

else:

    st.info(
        "No violations available"
    )

st.divider()

# ===================================
# REPORT STATUS
# ===================================

st.success(
    "✅ SafetyEye Reporting System Active"
)

# ===================================
# FOOTER
# ===================================

st.markdown(
"""
<hr>

<center>

<h3 style='color:orange'>
📄 SafetyEye Report Center
</h3>

<p>
Generate and download professional safety reports
</p>

</center>
""",
unsafe_allow_html=True
)