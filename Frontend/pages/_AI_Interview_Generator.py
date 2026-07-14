import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Interview Generator",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Interview Question Generator")
st.caption("Generate AI-powered interview questions based on Resume & Job Description")

st.divider()

candidate_response = requests.get(f"{API_URL}/candidate/")

candidate_data = []

if candidate_response.status_code == 200:
    candidate_data = candidate_response.json()["data"]

job_response = requests.get(f"{API_URL}/job/")

job_data = []

if job_response.status_code == 200:
    job_data = job_response.json()["data"]

candidate = st.selectbox(
    "👤 Select Candidate",
    candidate_data,
    format_func=lambda x: x["name"]
)


job = st.selectbox(
    "💼 Select Job",
    job_data,
    format_func=lambda x: x["job_title"]
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.info(f"👤 Candidate : {candidate['name']}")

with col2:
    st.info(f"💼 Job : {job['job_title']}")

st.divider()

if st.button("🚀 Generate Interview Questions", use_container_width=True):

    with st.spinner("Generating AI Questions..."):

        response = requests.get(
            f"{API_URL}/interview/{candidate['id']}/{job['id']}"
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Questions Generated Successfully!")

            st.subheader("📋 AI Interview Questions")

            st.text_area(
                "Questions",
                result["questions"],
                height=450
            )

        else:
            st.error(response.text)