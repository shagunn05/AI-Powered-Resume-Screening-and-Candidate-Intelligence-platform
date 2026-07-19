import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Interview Generator",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Interview Question Generator")
st.caption("Generate 5 AI-powered interview questions based on Candidate Resume & Job Description")

st.divider()


# -------------------------------
# Fetch Candidates
# -------------------------------

try:
    response = requests.get(f"{API_URL}/candidate/")

    if response.status_code == 200:
        candidate_data = response.json()["data"]
    else:
        candidate_data = []

except:
    st.error("❌ Backend is not running.")
    st.stop()


# -------------------------------
# Fetch Jobs
# -------------------------------

try:

    response = requests.get(f"{API_URL}/job/")

    if response.status_code == 200:
        job_data = response.json()["data"]

    else:
        job_data = []

except:

    st.error("Unable to fetch jobs.")
    st.stop()


if len(candidate_data) == 0:
    st.warning("No Candidates Found")
    st.stop()

if len(job_data) == 0:
    st.warning("No Jobs Found")
    st.stop()


# -------------------------------
# Selection
# -------------------------------

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

# -------------------------------
# Summary Cards
# -------------------------------

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

# -------------------------------
# Generate Button
# -------------------------------

if st.button("🚀 Generate AI Interview Questions", use_container_width=True):

    with st.spinner("AI is generating interview questions..."):

        response = requests.get(
            f"{API_URL}/interview/{candidate['id']}/{job['id']}"
        )

        if response.status_code == 200:

            result = response.json()

            st.success("✅ Interview Questions Generated")

            st.divider()

            st.subheader("📋 Top 5 Interview Questions")

            st.markdown(result["questions"])

            st.download_button(
                "📥 Download Questions",
                result["questions"],
                file_name="Interview_Questions.txt",
                mime="text/plain"
            )

        else:

            st.error(response.text)