import streamlit as st
import requests

# ==========================================
# Configuration
# ==========================================

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="TalentPilot AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# Fetch Dashboard Metrics
# ==========================================

candidate_count = 0
job_count = 0
report_count = 0
module_count = 8

try:

    response = requests.get(
        f"{API_URL}/analytics/",
        timeout=5
    )

    if response.status_code == 200:

        data = response.json()

        candidate_count = data["metrics"]["total_candidates"]
        job_count = data["metrics"]["total_jobs"]

except:
    pass


# ==========================================
# Sidebar
# ==========================================

with st.sidebar:

    st.title("🤖 TalentPilot AI")

    st.caption("Enterprise Recruitment Platform")

    st.divider()

    st.success("🟢 System Ready")

    st.divider()

    st.markdown("### 🚀 Available Modules")

    modules = [

        "📄 Resume Upload",
        "👥 Candidate Dashboard",
        "💼 Job Description",
        "🎯 ATS Matching",
        "🤖 AI Resume Analysis",
        "🎤 Interview Generator",
        "✅ Hiring Recommendation",
        "🏆 Candidate Ranking",
        "📊 Recruiter Analytics"

    ]

    for module in modules:

        st.write(module)

# ==========================================
# Hero Section
# ==========================================
st.markdown("""
<div style="text-align:center;line-height:1.05;">

<h1 style="margin:0;font-size:46px;font-weight:700;">
🤖 TalentPilot AI
</h1>

<p style="margin:0;color:#6B7280;font-size:18px;">
AI-Powered Resume Screening & Candidate Intelligence Platform
</p>

</div>
""", unsafe_allow_html=True)

st.divider()
# ==========================================
# Recruitment Dashboard
# ==========================================

st.subheader("📊 Recruitment Dashboard")

st.caption(
    "Real-time overview of recruitment activities and AI-powered hiring insights."
)

card1, card2, card3, card4 = st.columns(4)

with card1:

    with st.container(border=True):

        st.metric(
            label="👥 Candidates",
            value=candidate_count
        )

        st.caption("Registered Profiles")


with card2:

    with st.container(border=True):

        st.metric(
            label="💼 Job Openings",
            value=job_count
        )

        st.caption("Active Positions")


with card3:

    with st.container(border=True):

        st.metric(
            label="🤖 AI Modules",
            value=module_count
        )

        st.caption("Implemented Features")


with card4:

    with st.container(border=True):

        st.metric(
            label="📈 Reports",
            value=report_count
        )

        st.caption("Generated Analytics")


st.divider()

# ==========================================
# Technology Stack
# ==========================================

st.subheader("🛠 Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:

    with st.container(border=True):

        st.markdown("""
### ⚙ Backend

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
""")


with col2:

    with st.container(border=True):

        st.markdown("""
### 🤖 AI & ML

- Mistral AI
- LangChain
- Python
""")


with col3:

    with st.container(border=True):

        st.markdown("""
### 💻 Frontend

- Streamlit
- Pandas
- Plotly
""")

st.divider()

# ==========================================
# Platform Highlights
# ==========================================

st.subheader("✨ Platform Highlights")

left, right = st.columns(2)

with left:

    with st.container(border=True):

        st.markdown("""
### 🤖 AI Recruitment

✔ Resume Parsing

✔ Job Description Analysis

✔ ATS Matching

✔ AI Resume Analysis

✔ AI Interview Generator
""")


with right:

    with st.container(border=True):

        st.markdown("""
### 👨‍💼 Recruiter Tools

✔ Hiring Recommendation

✔ Candidate Ranking

✔ Recruiter Analytics

✔ FastAPI REST API

✔ PostgreSQL Database
""")

st.divider()


# ==========================================
# About TalentPilot AI
# ==========================================

st.subheader("ℹ️ About TalentPilot AI")

with st.container(border=True):

    st.write(
        """
TalentPilot AI is an intelligent recruitment platform that streamlines the hiring workflow using Artificial Intelligence.

From resume parsing and ATS matching to interview generation and hiring recommendations, the platform helps recruiters identify the most suitable candidates quickly, accurately, and efficiently.
"""
    )

st.divider()


# ==========================================
# Footer
# ==========================================

st.markdown(
"""
<div style="text-align:center;
padding:15px;
color:#6B7280;
font-size:14px;">

<b style="font-size:18px;">
🤖 TalentPilot AI
</b>

<br>

Enterprise AI Recruitment Platform

<br><br>

Built with FastAPI • Streamlit • PostgreSQL • LangChain • Mistral AI

<br><br>

© 2026 TalentPilot AI. All Rights Reserved.

</div>
""",
unsafe_allow_html=True
)