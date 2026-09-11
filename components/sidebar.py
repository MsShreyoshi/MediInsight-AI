import streamlit as st

NAV_ITEMS = [
    ("dashboard", "Dashboard", ":material/home:"),
    ("analytics", "Analytics", ":material/analytics:"),
    ("patients", "Patients", ":material/person_add:"),
    ("test_recommender", "Test Recommender", ":material/biotech:"),
    ("report_analyzer", "Report Analyzer", ":material/description:"),
]

def render_sidebar():
    st.markdown(
        '<div class="mi-sidebar-brand"><span class="mi-menu-icon">☰</span></div>',
        unsafe_allow_html=True,
    )

    for key, label, icon in NAV_ITEMS:
        if st.button(label, key=f"nav_{key}", icon=icon, use_container_width=True):
            st.session_state["page"] = key
            st.rerun()

    st.markdown('<div class="mi-sidebar-spacer"></div>', unsafe_allow_html=True)

    if st.button("Settings", key="nav_settings", icon=":material/settings:", use_container_width=True):
        st.session_state["page"] = "settings"
        st.rerun()

    if st.button("Logout", key="nav_logout", icon=":material/logout:", use_container_width=True):
        st.session_state.clear()
        st.rerun()
