import streamlit as st
import pandas as pd
import requests
import pandas as pd
import streamlit as st

API_URL = "http://127.0.0.1:8000/candidate/"

try:
    response = requests.get(API_URL)

    if response.status_code == 200:
        candidates = response.json()["data"]

        df = pd.DataFrame(candidates)

        st.dataframe(df, use_container_width=True)

    else:
        st.error("Unable to fetch candidates.")

except Exception as e:
    st.error(f"Backend not running: {e}")
# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Candidate Dashboard",
    page_icon="👥",
    layout="wide"
)

st.title("👥 Candidate Management Dashboard")
st.caption("AI-Powered Resume Screening Platform")

st.divider()

# -----------------------------
# Top Metrics
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Total Candidates", "0")

with col2:
    st.metric("⭐ Top Skill", "-")

with col3:
    st.metric("🆕 Recent Uploads", "0")

st.divider()

# -----------------------------
# Search & Filter
# -----------------------------
left, right = st.columns(2)

with left:
    search = st.text_input(
        "🔍 Search Candidate",
        placeholder="Enter candidate name..."
    )

with right:
    skill = st.selectbox(
        "🛠 Filter by Skill",
        [
            "All",
            "Python",
            "SQL",
            "FastAPI",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "LangChain"
        ]
    )

st.divider()

# -----------------------------
# Candidate Table
# -----------------------------
st.subheader("📋 Candidate List")

df = pd.DataFrame(
    columns=[
        "ID",
        "Name",
        "Email",
        "Phone",
        "Skills",
        "Uploaded At"
    ]
)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# -----------------------------
# Candidate Details
# -----------------------------
st.subheader("👤 Candidate Details")

st.info("Select a candidate after backend integration.")

st.divider()

# -----------------------------
# Actions
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.button("🗑 Delete Candidate", use_container_width=True)

with col2:
    st.button("📥 Download Resume", use_container_width=True) 