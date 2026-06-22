import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Safety Heatmap",
    page_icon="🔥",
    layout="wide"
)

st.title("🔥 Safety Heatmap")
st.subheader(
    "High Risk Zone Visualization"
)

np.random.seed(42)

data = pd.DataFrame({

    "X": np.random.randint(
        1,
        100,
        100
    ),

    "Y": np.random.randint(
        1,
        100,
        100
    ),

    "Violations": np.random.randint(
        1,
        10,
        100
    )
})
heatmap = px.density_heatmap(

    data,

    x="X",

    y="Y",

    z="Violations",

    nbinsx=20,

    nbinsy=20
)

st.plotly_chart(
    heatmap,
    use_container_width=True
)
st.subheader(
    "Zone Analysis"
)

z1,z2,z3 = st.columns(3)

with z1:

    st.error(
        "🔴 High Risk Zone"
    )

with z2:

    st.warning(
        "🟡 Medium Risk Zone"
    )

with z3:

    st.success(
        "🟢 Safe Zone"
    )
st.subheader(
    "AI Recommendation"
)

st.info(
    """
Monitor red zones closely.

Increase PPE compliance checks.

Reduce worker congestion in high-risk areas.
    """
)