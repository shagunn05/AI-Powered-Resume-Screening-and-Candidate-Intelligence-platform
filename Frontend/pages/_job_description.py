import streamlit as st
import requests

st.set_page_config(
    page_title="Job Description Upload",
    page_icon="📄",
    layout="wide"
)

API_BASE_URL = "http://127.0.0.1:8000"

st.title("📄 Job Description Upload")
st.caption("Upload a Job Description to extract required skills and requirements.")

st.divider()

uploaded_file = st.file_uploader(
    "Upload Job Description",
    type=["pdf"],
    help="Upload PDF Job Description"
)

if uploaded_file is not None:

    st.success(f"Selected File: {uploaded_file.name}")

    if st.button("🚀 Upload Job Description", use_container_width=True):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        try:

            with st.spinner("Uploading Job Description..."):

                response = requests.post(
                    f"{API_BASE_URL}/job/upload",
                    files=files
                )

            if response.status_code == 200:

                data = response.json()

                st.success("✅ Job Description Uploaded Successfully")

                job = data["job"]

                st.divider()

                st.subheader("📌 Job Details")

                col1, col2 = st.columns(2)

                with col1:

                    st.write("### 💼 Job Title")
                    st.info(job["job_title"])

                    st.write("### 🎓 Education")
                    st.info(job["education"])

                with col2:

                    st.write("### 💼 Experience")
                    st.info(job["experience"])

                    st.write("### 📅 Uploaded At")
                    st.info(job["uploaded_at"])

                st.divider()

                st.subheader("🛠 Required Skills")

                skills = job["required_skills"].split(",")

                cols = st.columns(3)

                for i, skill in enumerate(skills):

                    cols[i % 3].success(skill.strip())

            else:

                st.error(response.text)

        except Exception as e:

            st.error(e)