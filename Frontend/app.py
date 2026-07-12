import streamlit as st
import requests

st.set_page_config(
    page_title="TalentPilot AI",
    layout="wide"
)

st.title("🤖 TalentPilot AI")
st.subheader("Enterprise Agentic Recruitment Platform")

if st.button("Check Backend Status"):

    response = requests.get("http://127.0.0.1:8000/health")

    if response.status_code == 200:
        st.success("Backend Connected Successfully ✅")
        st.json(response.json())
    else:
        st.error("Backend Connection Failed")