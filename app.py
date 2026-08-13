import streamlit as st
from pathlib import Path


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="MediInsight AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

BACKGROUND_PATH = BASE_DIR / "assets" / "hospital_bg.png"
LOGO_PATH = BASE_DIR / "assets" / "medinsight_logo.png"


# ==========================================================
# CHECK ASSETS
# ==========================================================

if not BACKGROUND_PATH.exists():
    st.error(
        f"Background image not found:\n{BACKGROUND_PATH}"
    )
    st.stop()

if not LOGO_PATH.exists():
    st.error(
        f"Logo image not found:\n{LOGO_PATH}"
    )
    st.stop()


# ==========================================================
# SESSION STATE
# ==========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ==========================================================
# LOGIN PAGE
# ==========================================================

if not st.session_state.logged_in:

    # ------------------------------------------------------
    # PAGE TITLE
    # ------------------------------------------------------

    st.title("MediInsight AI")

    st.write("Welcome to MediInsight AI")

    st.divider()

    # ------------------------------------------------------
    # TWO COLUMN LAYOUT
    # ------------------------------------------------------

    left_column, right_column = st.columns(
        [1, 1.5],
        gap="large"
    )

    # ======================================================
    # LEFT COLUMN
    # ======================================================

    with left_column:

        st.image(
            BACKGROUND_PATH,
            use_container_width=True
        )

        st.image(
            LOGO_PATH,
            width=180
        )

        st.subheader("MediInsight AI")

        st.write(
            "Emergency Analytics & "
            "Medical Report Analyzer"
        )

    # ======================================================
    # RIGHT COLUMN
    # ======================================================

    with right_column:

        st.header("Welcome Back!")

        st.write("Sign in to continue")

        st.write("")

        username = st.text_input(
            "Email or Username",
            placeholder="Email or Username"
        )

        password = st.text_input(
            "Password",
            placeholder="Password",
            type="password"
        )

        remember_me = st.checkbox(
            "Remember me"
        )

        st.write("")

        sign_in = st.button(
            "Sign In",
            use_container_width=True
        )

        # --------------------------------------------------
        # LOGIN ACTION
        # --------------------------------------------------

        if sign_in:

            if not username.strip():
                st.warning(
                    "Please enter your username or email."
                )

            elif not password.strip():
                st.warning(
                    "Please enter your password."
                )

            elif (
                username == "doctor"
                and password == "1234"
            ):

                st.session_state.logged_in = True
                st.session_state.username = username

                st.rerun()

            else:

                st.error(
                    "Invalid username or password."
                )


# ==========================================================
# DASHBOARD PLACEHOLDER
# ==========================================================

else:

    st.title("MediInsight AI Dashboard")

    st.success(
        "You are successfully logged in."
    )

    st.write(
        f"Welcome, {st.session_state.get('username', 'Doctor')}!"
    )

    if st.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()