import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="ATS Matching",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 ATS Resume Matching")

# -------------------------
# Candidates
# -------------------------

candidate_response = requests.get(
    f"{API_URL}/candidate/"
)

candidate_data = candidate_response.json()["data"]

candidate_dict = {

    c["name"]: c["id"]

    for c in candidate_data

}

candidate = st.selectbox(

    "Select Candidate",

    candidate_dict.keys()

)

# -------------------------
# Jobs
# -------------------------

job_response = requests.get(

    f"{API_URL}/job/"

)

job_data = job_response.json()["data"]

job_dict = {

    j["job_title"]: j["id"]

    for j in job_data

}

job = st.selectbox(

    "Select Job",

    job_dict.keys()

)

# -------------------------

if st.button("Calculate ATS Score"):

    candidate_id = candidate_dict[candidate]

    job_id = job_dict[job]

    response = requests.get(

        f"{API_URL}/matching/{candidate_id}/{job_id}"

    )

    result = response.json()

    st.success("ATS Matching Completed")

    st.metric(

        "ATS Score",

        f"{result['match_score']} %"

    )

    st.subheader("Matched Skills")

    st.success(

        ", ".join(

            result["matched_skills"]

        )

    )

    st.subheader("Missing Skills")

    st.error(

        ", ".join(

            result["missing_skills"]

        )

    )

    st.subheader("Recommendation")

    st.info(

        result["recommendation"]

    )