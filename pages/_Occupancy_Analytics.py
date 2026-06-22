import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("👥 Occupancy Analytics")

if os.path.exists("occupancy_log.csv"):

    df = pd.read_csv("occupancy_log.csv")

    if len(df) > 0:

        st.subheader("Occupancy Trend")

        fig = px.line(
            df,
            x="Time",
            y="Occupancy",
            markers=True
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("Occupancy Data")

        st.dataframe(df)

    else:
        st.warning("No occupancy data available.")

else:
    st.error("occupancy_log.csv not found.")