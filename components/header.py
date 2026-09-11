import streamlit as st

def render_header():
    user = st.session_state.get("user", {})
    name = user.get("name", "Doctor")

    st.html(f"""
    <div class="mi-header">
        <div class="mi-brand">
            <img src="data:image/png;base64,{st.session_state.get('logo_b64', '')}" />
            <span>MediInsight <b>AI</b></span>
        </div>
        <div class="mi-header-right">
            <span class="mi-bell">♧</span>
            <div class="mi-avatar">👨‍⚕️</div>
            <span class="mi-user-name">{name}</span>
        </div>
    </div>
    """)
