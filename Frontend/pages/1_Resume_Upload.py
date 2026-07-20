import streamlit as st
import requests

# ==========================================
# Configuration
# ==========================================

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Resume Upload",
    page_icon="📄",
    layout="wide"
)

# ==========================================
# Header
# ==========================================

st.title("📄 Resume Upload")

st.caption(
    "Upload candidate resumes for AI-powered parsing and recruitment analysis."
)

st.divider()

# ==========================================
# Upload Section
# ==========================================

uploaded_file = st.file_uploader(
    "Choose Resume",
    type=["pdf", "docx"]
)

if uploaded_file is not None:

    st.success(f"Selected File: **{uploaded_file.name}**")

    if st.button("🚀 Upload Resume", use_container_width=True):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        try:

            with st.spinner("Uploading Resume..."):

                response = requests.post(
                    f"{API_BASE_URL}/upload/resume",
                    files=files,
                    timeout=30
                )

            if response.status_code == 200:

                data = response.json()

                st.success("✅ Resume Uploaded Successfully")

                candidate = data["candidate"]

                st.divider()

                st.subheader("👤 Candidate Information")

                col1, col2 = st.columns(2)

                with col1:

                    with st.container(border=True):

                        st.write("**Name**")
                        st.write(candidate.get("name", "Not Available"))

                        st.write("**Email**")
                        st.write(candidate.get("email", "Not Available"))

                with col2:

                    with st.container(border=True):

                        st.write("**Phone**")
                        st.write(candidate.get("phone", "Not Available"))

                        st.write("**Uploaded At**")
                        st.write(candidate.get("uploaded_at", "Not Available"))

                st.divider()

                st.subheader("🛠 Extracted Skills")

                skills = candidate.get("skills")

                if skills:

                    if isinstance(skills, str):
                        skills = [skill.strip() for skill in skills.split(",")]

                    cols = st.columns(3)

                    for i, skill in enumerate(skills):
                        with cols[i % 3]:
                            st.success(skill)

                else:
                    st.warning("No skills found.")

            else:

                st.error(f"❌ Upload Failed ({response.status_code})")

                try:
                    st.json(response.json())
                except:
                    st.text(response.text)

        except requests.exceptions.ConnectionError:

            st.error("❌ Cannot connect to FastAPI Backend.")

            st.info(
                "Please make sure the backend server is running.\n\n"
                "Backend URL:\n"
                "`http://127.0.0.1:8000`"
            )

        except requests.exceptions.Timeout:

            st.error("⏳ Request Timed Out.")

        except Exception as e:

            st.exception(e)