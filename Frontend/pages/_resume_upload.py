import streamlit as st
import requests
from utils.config import API_BASE_URL

st.set_page_config(
    page_title="Resume Upload",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Upload")
st.write("Upload candidate resumes for AI screening.")

uploaded_file = st.file_uploader(
    "Choose Resume",
    type=["pdf", "docx"]
)

if uploaded_file is not None:

    st.success(f"Selected File: {uploaded_file.name}")

    if st.button("🚀 Upload Resume", use_container_width=True):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }
        response = requests.post(
               f"{API_BASE_URL}/upload/resume",
               files=files
        )

        try:

            with st.spinner("Uploading Resume..."):

                response = requests.post(
                    "http://127.0.0.1:8000/upload/resume",
                    files=files
                )

            if response.status_code == 200:

                data = response.json()

                st.success("Resume Uploaded Successfully ✅")

                candidate = data["candidate"]

                st.subheader("Candidate Information")

                st.write(f"**Name:** {candidate['name']}")
                st.write(f"**Email:** {candidate['email']}")
                st.write(f"**Phone:** {candidate['phone']}")
                st.write(f"**Skills:** {candidate['skills']}")

            else:

                st.error(response.text)

        except Exception as e:

            st.error(e)