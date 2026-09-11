import streamlit as st
import base64
from pathlib import Path
from utils.authentication import login

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).parent

BACKGROUND_PATH = BASE_DIR / "assets" / "hospital_bg.png"
LOGO_PATH = BASE_DIR / "assets" / "medinsight_logo.png"
LOGIN_CSS_PATH = BASE_DIR / "css" / "login.css"

# ==========================================================
# CONFIG
# ==========================================================

st.set_page_config(
    page_title="MediInsight AI",
    page_icon=LOGO_PATH,
    layout="wide",
    initial_sidebar_state="collapsed",
)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden;}
       footer {visibility: hidden;}
       header {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


# ==========================================================
# ASSET LOADER
# ==========================================================

def image_to_base64(path: Path) -> str:

    with open(path, "rb") as image:

        return base64.b64encode(
            image.read()
        ).decode("utf-8")

def load_css(path: Path):
    return path.read_text(encoding="utf-8")

background = image_to_base64(BACKGROUND_PATH)
logo = image_to_base64(LOGO_PATH)

def app_shell():
    from components.sidebar import render_sidebar
    from components.header import render_header
    from pages.dashboard import render as render_dashboard

    render_sidebar()
    render_header()

    page = st.session_state.get("page", "dashboard")
    st.markdown('<div class="mi-content">', unsafe_allow_html=True)

    if page == "dashboard":
        render_dashboard()
    else:
        st.info(
            f"{page.replace('_', ' ').title()} page is next. "
            "We will build it from the Figma reference."
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# PAGE CSS
# ==========================================================

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "page" not in st.session_state:
    st.session_state["page"] = "login"

if not st.session_state["authenticated"]:
    login_css = load_css(LOGIN_CSS_PATH)
    login_css = login_css.replace(
        "{{BACKGROUND_IMAGE}}",
        f"data:image/png;base64,{background}"
    )
    st.html(
        f"""
        <style>
        {login_css}
        </style>

        <!-- ====================================================
            FIGMA CANVAS
        ===================================================== -->

        <div class="mediinsight-canvas">

        <!-- LEFT -->

        <div class="branding-panel">

        <img src="data:image/png;base64,{logo}" class="branding-logo">

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


        <!-- RIGHT -->

        <div class="login-content">

        <div class="login-title"> Welcome Back! </div>

        <div class="login-subtitle"> Sign in to continue </div>


        <div class="form-area">

        <div class="username-placeholder"> </div>

        <div class="password-placeholder"> </div>

        <div class="login-button"> Log In </div>

        </div>

        </div>

        </div>
        """
    )

    username = st.text_input(
        "Username",
        placeholder="Email or username",
        label_visibility="collapsed",
        key="login_username",
    )

    password = st.text_input(
        "Password",
        placeholder="Password",
        label_visibility="collapsed",
        key="login_password",
        type="password"
    )

    remember_me = st.checkbox(
        "Remember me",
        key="remember_me",
    )

    log_in = st.button(
        "Log In",
        key="log_in",
    )

    if log_in:

        if not username or not password:

            st.error("Please enter your username and password.")

        else:

            # Check credentials
            success, user = login(username, password)

            if success:

                # Store login information
                st.session_state["authenticated"] = True
                st.session_state["user"] = user

                # Open dashboard
                st.session_state["page"] = "dashboard"

                # Refresh application
                st.rerun()

            else:

                st.error("Invalid username or password.")

else:
    app_shell()            

