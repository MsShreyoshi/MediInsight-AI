import streamlit as st
from pathlib import Path
import base64


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
# LOAD BACKGROUND IMAGE
# ==========================================================

with open(BACKGROUND_PATH, "rb") as image_file:

    background_base64 = base64.b64encode(
        image_file.read()
    ).decode()


# ==========================================================
# SESSION STATE
# ==========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


# ==========================================================
# LOAD CSS
# ==========================================================

CSS_PATH = BASE_DIR / "css" / "login.css"

with open(
    CSS_PATH,
    "r",
    encoding="utf-8"
) as css_file:

    login_css = css_file.read()


login_css = login_css.replace(
    "REPLACE_BACKGROUND",
    background_base64
)


st.markdown(
    f"<style>{login_css}</style>",
    unsafe_allow_html=True,
)


# ==========================================================
# DASHBOARD
# ==========================================================

if st.session_state.logged_in:

    st.title("MediInsight AI Dashboard")

    st.success("Login successful.")

    st.write(
        f"Welcome, {st.session_state.username}!"
    )

    st.write(
        "The dashboard will be built in the next phase."
    )

    if st.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.username = ""

        st.rerun()

    st.stop()


# ==========================================================
# LOGIN PAGE
# ==========================================================

left_column, right_column = st.columns(
    [2, 4],
    gap="large",
)


# ==========================================================
# LEFT SIDE
# ==========================================================

with left_column:

    st.markdown(
        """
        <div class="branding-panel">

        <div class="branding-content">

        <img src="data:image/png;base64,REPLACE_LOGO" class="branding-logo">

        <div class="branding-title">
        <span class="branding-black"> MediInsight </span>
        <span class="branding-red"> AI </span>
        </div>

        <div class="branding-tagline">
        Emergency Analytics
        <br>
        &
        <br>
        Medical Report Analyzer
        </div>

        </div>

        </div>
        """.replace(
            "REPLACE_LOGO",
            base64.b64encode(
                LOGO_PATH.read_bytes()
            ).decode()
        ),
        unsafe_allow_html=True
    )


# ==========================================================
# RIGHT SIDE
# ==========================================================

with right_column:

    st.title("Welcome Back!")

    st.write("Sign in to continue")

    st.write("")

    username = st.text_input(
        "Email or Username",
        placeholder="Email or Username",
    )

    password = st.text_input(
        "Password",
        placeholder="Password",
        type="password",
    )

    remember_me = st.checkbox(
        "Remember me"
    )

    st.write("")

    sign_in = st.button(
        "Sign In",
        use_container_width=True,
    )


    # ======================================================
    # LOGIN VALIDATION
    # ======================================================

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