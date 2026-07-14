import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Recruiter Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Recruiter Analytics Dashboard")
st.caption("Monitor recruitment insights with AI-powered analytics")

response = requests.get(f"{API_URL}/analytics/")

if response.status_code != 200:
    st.error("Unable to load analytics.")
    st.stop()

result = response.json()

metrics = result["metrics"]

skills = result["top_skills"]

st.divider()

c1, c2 = st.columns(2)

with c1:
    st.metric(
        "👥 Total Candidates",
        metrics["total_candidates"]
    )

with c2:
    st.metric(
        "💼 Total Jobs",
        metrics["total_jobs"]
    )

st.divider()

st.subheader("🔥 Most Common Skills")

df = pd.DataFrame(
    list(skills.items()),
    columns=["Skill", "Count"]
)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.subheader("📈 Skill Distribution")

chart = df.set_index("Skill")

st.bar_chart(chart)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Skill Report",
    csv,
    file_name="analytics.csv",
    mime="text/csv"
)


