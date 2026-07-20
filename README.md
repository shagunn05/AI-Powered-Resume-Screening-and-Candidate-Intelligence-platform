# 🤖 TalentPilot AI

### AI-Powered Resume Screening & Candidate Intelligence Platform

TalentPilot AI is an AI-powered recruitment platform that automates resume screening, ATS matching, AI resume analysis, interview generation, hiring recommendation, and candidate ranking.

---

# 🌐 Live Demo

🚀 https://ai-powered-resume-screening-and-candidate-intelligence-platfor.streamlit.app/

---

# 📸 Project Preview

## 🏠 Recruitment Dashboard

![Recruitment Dashboard](assets/(1)dashborad.png)

---

## 📊 Dashboard Overview

![Dashboard Overview](assets/(2)dashborad.png)

---

## 📄 Resume Upload

![Resume Upload](assets/(3)resume_upload.png)

---

## 👥 Candidate Dashboard

![Candidate Dashboard](assets/(4)candidate%20dashborad.png)

![Candidate Dashboard](assets/(5)candidate%20dashborad.png)

---

## 💼 Job Description

![Job Description](assets/(6)job%20description.png)

---

## 🎯 ATS Matching

![ATS Matching](assets/(7)%20ats%20matching.png)

---

## 🤖 AI Resume Analysis

![AI Resume Analysis](assets/(8)%20ai%20analysis.png)

---

## 🎤 AI Interview Generator

![Interview Generator](assets/(9)%20ai%20interview%20generator.png)

---

## ✅ AI Hiring Recommendation

![Hiring Recommendation](assets/(10)%20ai%20hiring%20recommendation.png)

---

## 🏆 Candidate Ranking

![Candidate Ranking](assets/(11)%20candidate%20ranking.png)

![Candidate Ranking](assets/(12)%20candidate%20ranking.png)

---

## 📈 Recruiter Analytics

![Recruiter Analytics](assets/(13)%20recruiter%20analytical.png)

---

# ✨ Features

- 📄 Resume Upload
- 👥 Candidate Dashboard
- 💼 Job Description Parsing
- 🎯 ATS Matching
- 🤖 AI Resume Analysis
- 🎤 AI Interview Generator
- ✅ Hiring Recommendation
- 🏆 Candidate Ranking
- 📊 Recruiter Analytics
- 🐳 Dockerized Backend & Frontend
- ⚡ Multi-container Application using Docker Compose

---

# 🛠 Tech Stack

### Frontend
- Streamlit
- Pandas
- Plotly

### Backend
- FastAPI
- SQLAlchemy
- Pydantic

### Database
- PostgreSQL

### AI
- LangChain
- Mistral AI
- Python

### DevOps
- Docker
- Docker Compose

---

# 📂 Project Structure

```text
TalentPilot-AI
│
├── Backend
│   ├── Dockerfile
│   └── ...
│
├── Frontend
│   ├── Dockerfile
│   └── ...
│
├── assets
├── Uploads
├── Vector-Db
├── docker-compose.yml
├── .dockerignore
├── README.md
├── LICENSE
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/shagunn05/AI-Powered-Resume-Screening-and-Candidate-Intelligence-platform.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Backend

```bash
uvicorn Backend.api.main:app --reload
```

### Run Frontend

```bash
streamlit run Frontend/app.py
```

---

# 🐳 Run with Docker

### Build and Start All Containers

```bash
docker compose up --build
```

### Run in Detached Mode

```bash
docker compose up -d
```

### Stop Containers

```bash
docker compose down
```

### View Running Containers

```bash
docker ps
```

### Services

| Service | Port |
|----------|------|
| FastAPI Backend | 8000 |
| Streamlit Frontend | 8501 |
| PostgreSQL | 5432 |

---

# 🔮 Future Improvements

- User Authentication
- Email Notifications
- AI Chat Assistant
- Resume Score Prediction
- Cloud Deployment
- Multi-language Resume Parsing

---

# 👩‍💻 Author

**Shagun Sharma**

Aspiring AI/ML Engineer | Data Scientist

### GitHub
https://github.com/shagunn05

### Live Demo
https://ai-powered-resume-screening-and-candidate-intelligence-platfor.streamlit.app/

---

# 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project helpful, don't forget to star the repository.