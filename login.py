import streamlit as st
from datetime import datetime
import os

st.set_page_config(
    page_title="SafetyEye Login",
    page_icon="🔐",
    layout="centered"
)

# ==================================
# THEME
# ==================================

st.markdown("""
<style>

.stApp{
background:linear-gradient(
135deg,
#050816,
#0b1020,
#121b35
);
}

h1{
color:white;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# TITLE
# ==================================

st.title("🔐 SafetyEye Login")

st.write("")

# ==================================
# CREATE LOGIN HISTORY FILE
# ==================================

if not os.path.exists(
    "login_history.csv"
):

    with open(
        "login_history.csv",
        "w"
    ) as f:

        f.write(
            "Time,Username\n"
        )

# ==================================
# LOGIN FORM
# ==================================

username = st.text_input(
    "Username"
)

password = st.text_input(
    "Password",
    type="password"
)

# ==================================
# USERS
# ==================================

users = {

    "admin":"admin123",

    "supervisor":"super123",
    
    "yuvanesh":"yuvanesh2906"

}

# ==================================
# LOGIN BUTTON
# ==================================

if st.button("Login"):

    if (
        username in users
        and
        users[username] == password
    ):

        # Save Login Record

        with open(
            "login_history.csv",
            "a"
        ) as f:

            f.write(
                f"{datetime.now()},{username}\n"
            )

        st.success(
            f"✅ Welcome {username}"
        )

        try:

            st.switch_page(
                "pages/dashboard.py"
            )

        except:

            st.info(
                "Open Dashboard manually"
            )

    else:

        st.error(
            "❌ Invalid Username or Password"
        )

# ==================================
# SHOW LOGIN HISTORY
# ==================================

st.divider()

if st.checkbox(
    "Show Login History"
):

    import pandas as pd

    try:

        history = pd.read_csv(
            "login_history.csv"
        )

        st.dataframe(
            history,
            use_container_width=True
        )

    except:

        st.warning(
            "No login records"
        )

# ==================================
# FOOTER
# ==================================

st.markdown("""
<hr>

<center>

<h3 style='color:#ff8c00'>
🦺 SafetyEye AI Monitoring System
</h3>

<p style='color:white'>
AI Powered Workplace Safety Monitoring
</p>

</center>
""",
unsafe_allow_html=True)