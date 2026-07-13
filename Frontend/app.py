import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="TalentPilot AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🤖 TalentPilot AI")
st.sidebar.markdown("---")

st.sidebar.info(
    """
    **AI-Powered Recruitment Platform**

    Features:
    - 📄 Resume Upload
    - 👥 Candidate Dashboard
    - 📑 Job Description Analysis
    - 🎯 ATS Score
    - 🤖 AI Resume Analysis
    """
)

# -----------------------------
# Main Page
# -----------------------------
st.title("🚀 TalentPilot AI")
st.subheader("Enterprise AI Resume Screening System")

st.markdown("---")

st.markdown("""
### Welcome!

TalentPilot AI is an AI-powered recruitment platform designed to help recruiters:

- 📄 Upload and parse resumes
- 👥 Manage candidates
- 📑 Analyze Job Descriptions
- 🎯 Calculate ATS Match Score
- 🤖 Get AI-powered resume insights
- 🏆 Rank candidates automatically

Use the **sidebar** to navigate between pages.
""")

st.success("✅ Backend Connected (once FastAPI is running)")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Resumes", "0")

with col2:
    st.metric("👥 Candidates", "0")

with col3:
    st.metric("🎯 ATS Matches", "0")

st.markdown("---")

st.info("This dashboard will be updated dynamically as you continue building the project.")