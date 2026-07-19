import streamlit as st
import requests

API = "http://127.0.0.1:8000"

candidate_response = requests.get(f"{API}/candidate/")

candidate_data = []

if candidate_response.status_code == 200:
    candidate_data = candidate_response.json()["data"]

candidate = st.selectbox(
    "Select Candidate",
    candidate_data,
    format_func=lambda x: x["name"]
)

job_response = requests.get(f"{API}/job/")

job_data = []

if job_response.status_code == 200:
    job_data = job_response.json()["data"]

job = st.selectbox(
    "Select Job",
    job_data,
    format_func=lambda x: x["job_title"]
)

if st.button("🤖 Analyze Resume"):

    response = requests.get(
        f"{API}/analysis/{candidate['id']}/{job['id']}"
    )

    if response.status_code == 200:

        result = response.json()

        st.success("Analysis Completed!")

        st.markdown(result["analysis"])

    else:
        st.error("Analysis Failed")

        