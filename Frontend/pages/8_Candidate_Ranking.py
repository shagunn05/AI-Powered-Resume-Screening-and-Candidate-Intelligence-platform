import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Candidate Ranking",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Candidate Ranking Dashboard")
st.caption("Rank candidates based on Job Requirements")

st.divider()

# --------------------------------------------
# Fetch Jobs
# --------------------------------------------

try:

    response = requests.get(f"{API_URL}/job/")

    if response.status_code == 200:
        jobs = response.json()["data"]

    else:
        jobs = []

except Exception:

    st.error("❌ Backend is not running.")
    st.stop()

if len(jobs) == 0:

    st.warning("No Job Descriptions Found.")

    st.stop()

# --------------------------------------------
# Select Job
# --------------------------------------------

selected_job = st.selectbox(

    "💼 Select Job",

    jobs,

    format_func=lambda x: x["job_title"]

)

st.divider()

# --------------------------------------------
# Generate Ranking
# --------------------------------------------

if st.button("🚀 Generate Candidate Ranking", use_container_width=True):

    with st.spinner("Ranking Candidates..."):

        response = requests.get(

            f"{API_URL}/ranking/{selected_job['id']}"

        )

        if response.status_code == 200:

            result = response.json()

            st.success("Candidate Ranking Generated Successfully")

            st.divider()

            # --------------------------------------------
            # Metrics
            # --------------------------------------------

            col1, col2 = st.columns(2)

            with col1:

                st.metric(

                    "💼 Job",

                    result["job_title"]

                )

            with col2:

                st.metric(

                    "👥 Total Candidates",

                    result["total_candidates"]

                )

            st.divider()

            ranking = result["ranking"]

            # --------------------------------------------
            # Top Candidate
            # --------------------------------------------

            best = ranking[0]

            st.subheader("🥇 Top Candidate")

            c1, c2, c3 = st.columns(3)

            with c1:

                st.metric(

                    "Candidate",

                    best["name"]

                )

            with c2:

                st.metric(

                    "Match Score",

                    f"{best['score']}%"

                )

            with c3:

                st.metric(

                    "Recommendation",

                    best["recommendation"]

                )

            st.divider()

            # --------------------------------------------
            # Ranking Table
            # --------------------------------------------

            st.subheader("📋 Candidate Ranking")

            df = pd.DataFrame(ranking)

            df = df[
                [
                    "rank",
                    "name",
                    "score",
                    "recommendation",
                    "level"
                ]
            ]

            df.columns = [

                "Rank",

                "Candidate",

                "Match Score",

                "Recommendation",

                "Level"

            ]

            st.dataframe(

                df,

                use_container_width=True,

                hide_index=True

            )

            st.divider()

            # --------------------------------------------
            # Leaderboard
            # --------------------------------------------

            st.subheader("🏅 Leaderboard")

            medals = {

                1: "🥇",

                2: "🥈",

                3: "🥉"

            }

            for row in ranking:

                medal = medals.get(row["rank"], "🏅")

                st.write(

                    f"{medal} **Rank {row['rank']}** - "
                    f"{row['name']} | "
                    f"Score: **{row['score']}%** | "
                    f"{row['recommendation']} | "
                    f"{row['level']}"

                )

            st.divider()

            # --------------------------------------------
            # Match Score Chart
            # --------------------------------------------

            st.subheader("📊 Match Score Chart")

            chart = pd.DataFrame(

                {

                    "Candidate": [x["name"] for x in ranking],

                    "Match Score": [x["score"] for x in ranking]

                }

            )

            chart = chart.set_index("Candidate")

            st.bar_chart(chart)

            st.divider()

            # --------------------------------------------
            # Download CSV
            # --------------------------------------------

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(

                "📥 Download Ranking CSV",

                csv,

                file_name="candidate_ranking.csv",

                mime="text/csv"

            )

        else:

            st.error(response.text)