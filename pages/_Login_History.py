import streamlit as st
import pandas as pd
import os

st.title("🔐 Login History")

if os.path.exists(
    "login_history.csv"
):

    df = pd.read_csv(
        "login_history.csv"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.warning(
        "No login records found"
    )