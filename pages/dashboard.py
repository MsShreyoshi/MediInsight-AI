import streamlit as st
import pandas as pd

DEMO_PATIENTS = pd.DataFrame([
    {"id":"P001","severity":"Critical","diagnosis":"Pneumonia","status":"Admitted"},
    {"id":"P002","severity":"High","diagnosis":"Bronchitis","status":"Admitted"},
    {"id":"P003","severity":"Medium","diagnosis":"Viral Fever","status":"Admitted"},
    {"id":"P004","severity":"Medium","diagnosis":"Gastritis","status":"Admitted"},
    {"id":"P005","severity":"Low","diagnosis":"Migraine","status":"Discharged"},
    {"id":"P006","severity":"Low","diagnosis":"URTI","status":"Admitted"},
    {"id":"P007","severity":"Medium","diagnosis":"Asthma","status":"Admitted"},
    {"id":"P008","severity":"Medium","diagnosis":"UTI","status":"Discharged"},
    {"id":"P009","severity":"High","diagnosis":"Pneumonia","status":"Admitted"},
    {"id":"P010","severity":"Low","diagnosis":"Allergy","status":"Discharged"},
    {"id":"P011","severity":"Medium","diagnosis":"Diabetes","status":"Admitted"},
    {"id":"P012","severity":"Low","diagnosis":"Anemia","status":"Discharged"},
    {"id":"P013","severity":"Medium","diagnosis":"Gastritis","status":"Admitted"},
    {"id":"P014","severity":"Low","diagnosis":"URTI","status":"Admitted"},
])

def render():
    st.markdown('<div class="mi-page-title">Dashboard</div>', unsafe_allow_html=True)

    total = len(DEMO_PATIENTS)
    discharged = int((DEMO_PATIENTS["status"] == "Discharged").sum())
    critical = int((DEMO_PATIENTS["severity"] == "Critical").sum())

    cards = [
        ("Total Patients", total),
        ("Discharged", discharged),
        ("Critical Cases", critical),
        ("Bed Occupancy", "78%"),
        ("Average Wait Time", "24 min"),
        ("Pending Reports", 5),
    ]

    cols = st.columns(3, gap="large")
    for i, (label, value) in enumerate(cards):
        with cols[i % 3]:
            st.markdown(
                f'<div class="mi-kpi"><div class="mi-kpi-label">{label}</div><div class="mi-kpi-value">{value}</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
    left, right = st.columns(2, gap="large")

    with left:
        st.markdown('<div class="mi-panel-title">Patients by Severity</div>', unsafe_allow_html=True)
        sev = DEMO_PATIENTS["severity"].value_counts().reindex(
            ["Critical","High","Medium","Low"], fill_value=0
        )
        st.bar_chart(pd.DataFrame({"Patients": sev}), height=220)

    with right:
        st.markdown('<div class="mi-panel-title">Top Diagnoses</div>', unsafe_allow_html=True)
        diag = DEMO_PATIENTS["diagnosis"].value_counts().head(6).sort_values()
        st.bar_chart(pd.DataFrame({"Patients": diag}), height=220)
