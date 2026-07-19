import streamlit as st
import pandas as pd
import requests
from collections import Counter

st.set_page_config(
    page_title="Candidate Dashboard",
    page_icon="👥",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/candidate"

st.title("👥 Candidate Management Dashboard")
st.caption("AI Powered Resume Screening Platform")

st.divider()

# ------------------------
# Fetch Data
# ------------------------

try:
    response = requests.get(API_URL)

    if response.status_code == 200:

        response_data = response.json()

        candidates = response_data["data"]

        df = pd.DataFrame(candidates)

    else:
        st.error("Unable to fetch candidate data.")
        st.stop()

except Exception as e:
    st.error(f"Backend Not Running\n\n{e}")
    st.stop()


# ------------------------
# Metrics
# ------------------------

total_candidates = len(df)

all_skills = []

for skills in df["skills"]:
    if skills:
        all_skills.extend(
            [skill.strip() for skill in skills.split(",")]
        )

top_skill = "-"

if len(all_skills) > 0:
    top_skill = Counter(all_skills).most_common(1)[0][0]

recent_uploads = len(df)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Total Candidates", total_candidates)

with col2:
    st.metric("⭐ Top Skill", top_skill)

with col3:
    st.metric("🆕 Recent Uploads", recent_uploads)

st.divider()

# ------------------------
# Search + Filter
# ------------------------

left, right = st.columns(2)

with left:
    search = st.text_input(
        "🔍 Search Candidate"
    )

skill_options = ["All"] + sorted(list(set(all_skills)))

with right:

    selected_skill = st.selectbox(
        "🛠 Filter Skill",
        skill_options
    )

filtered_df = df.copy()

if search:
    filtered_df = filtered_df[
        filtered_df["name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

if selected_skill != "All":

    filtered_df = filtered_df[
        filtered_df["skills"].str.contains(
            selected_skill,
            case=False,
            na=False
        )
    ]

st.divider()

# ------------------------
# Candidate Table
# ------------------------

st.subheader("📋 Candidate List")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ------------------------
# Candidate Details
# ------------------------

st.subheader("👤 Candidate Details")

if len(filtered_df) > 0:

    selected = st.selectbox(
        "Select Candidate",
        filtered_df["name"]
    )

    candidate = filtered_df[
        filtered_df["name"] == selected
    ].iloc[0]

    st.write("### Candidate Information")

    st.write(f"**ID :** {candidate['id']}")
    st.write(f"**Name :** {candidate['name']}")
    st.write(f"**Email :** {candidate['email']}")
    st.write(f"**Phone :** {candidate['phone']}")
    st.write(f"**Skills :** {candidate['skills']}")
    st.write(f"**Uploaded :** {candidate['uploaded_at']}")

else:
    st.info("No Candidate Found.")

st.divider()

# ------------------------
# Actions
# ------------------------

col1, col2 = st.columns(2)

with col1:

    if st.button("🗑 Delete Candidate"):

        st.warning("Connect Delete API")

with col2:

    if st.button("📥 Download Resume"):

        st.info("Connect Resume Download API")