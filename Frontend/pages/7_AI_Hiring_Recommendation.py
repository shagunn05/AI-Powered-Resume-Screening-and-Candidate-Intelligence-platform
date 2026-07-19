import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Hiring Recommendation",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Hiring Recommendation")
st.caption("AI-powered hiring recommendation based on Candidate Resume & Job Description")

st.divider()

# ---------------------------------------------------
# Fetch Candidates
# ---------------------------------------------------

try:
    candidate_response = requests.get(f"{API_URL}/candidate/")

    if candidate_response.status_code == 200:
        candidate_data = candidate_response.json()["data"]
    else:
        candidate_data = []

except Exception:
    st.error("❌ Backend is not running.")
    st.stop()

# ---------------------------------------------------
# Fetch Jobs
# ---------------------------------------------------

try:
    job_response = requests.get(f"{API_URL}/job/")

    if job_response.status_code == 200:
        job_data = job_response.json()["data"]
    else:
        job_data = []

except Exception:
    st.error("❌ Unable to fetch jobs.")
    st.stop()

if not candidate_data:
    st.warning("No Candidates Available.")
    st.stop()

if not job_data:
    st.warning("No Jobs Available.")
    st.stop()

# ---------------------------------------------------
# Selection
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    candidate = st.selectbox(
        "👤 Select Candidate",
        candidate_data,
        format_func=lambda x: x["name"]
    )

with col2:
    job = st.selectbox(
        "💼 Select Job",
        job_data,
        format_func=lambda x: x["job_title"]
    )

st.divider()

# ---------------------------------------------------
# Candidate Summary
# ---------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("👤 Candidate Summary")

    st.success(f"""
**Name**

{candidate['name']}

**Email**

{candidate['email']}

**Phone**

{candidate['phone']}

**Skills**

{candidate['skills']}
""")

# ---------------------------------------------------
# Job Summary
# ---------------------------------------------------

with right:

    st.subheader("💼 Job Summary")

    st.info(f"""
**Job Title**

{job['job_title']}

**Required Skills**

{job['required_skills']}

**Experience**

{job['experience']}

**Education**

{job['education']}
""")

st.divider()

# ---------------------------------------------------
# Generate Recommendation
# ---------------------------------------------------

if st.button("🚀 Generate AI Hiring Recommendation", use_container_width=True):

    with st.spinner("Analyzing Candidate..."):

        response = requests.get(
            f"{API_URL}/recommendation/{candidate['id']}/{job['id']}"
        )

        if response.status_code == 200:

            result = response.json()

            st.success("✅ Recommendation Generated Successfully")

            st.divider()

            st.subheader("📋 AI Hiring Report")

            st.markdown(result["recommendation"])

            st.download_button(
                label="📥 Download Recommendation",
                data=result["recommendation"],
                file_name="AI_Hiring_Recommendation.txt",
                mime="text/plain"
            )

        else:

            st.error(response.text)