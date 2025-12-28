AI‑Powered Resume–Job Matching Engine
An end‑to‑end, containerized web application that semantically matches resumes to job descriptions using NLP and ML, built with FastAPI, React, and Docker.

Overview
Upload a resume and job description from the browser.

Backend extracts text, generates embeddings, and computes a semantic match score.

Frontend shows ranked results with explanations to help recruiters understand why a candidate is a strong fit.

Tech Stack
Frontend: React, TypeScript, Tailwind CSS, Axios

Backend: Python, FastAPI, Uvicorn, Pydantic

NLP: spaCy (en_core_web_sm), regex‑based parsing

ML / Similarity: sentence‑transformers (SBERT), scikit‑learn, NumPy

Infrastructure: Docker, docker‑compose, PostgreSQL (extensible), pdfplumber, python‑docx

Architecture
Frontend (React)

Single‑page UI for uploading resume and JD files.

Shows similarity score, extracted skills, and key highlights.

Backend (FastAPI)

REST APIs for file upload, processing, and scoring.

Orchestrates NLP pipeline and similarity computation.

NLP & ML layer

Cleans and normalizes text.

Uses spaCy for tokenization, lemmatization, and entity detection.

Uses SBERT embeddings + cosine similarity to compute a semantic match score.

Storage

Currently stateless by default; designed to plug in PostgreSQL for persisting resumes, JDs, and match history.

Features
Upload PDF/DOCX resumes and job descriptions.

Automatic skill, education, and experience extraction from text.

Semantic similarity scoring using sentence embeddings (beyond keyword matching).

Dockerized deployment with separate containers for frontend, backend, and database.

Running Locally with Docker
Prerequisites:

Docker and Docker Compose installed.

Steps:

bash
# Clone the repository
git clone https://github.com/suryaoruganti007/resume-job-matcher.git
cd resume-job-matcher

# Build and start all services
docker-compose up --build
Then:

Frontend: open http://localhost:3000

Backend API docs (FastAPI Swagger): http://localhost:8000/docs

Local Development (without Docker)
Backend
bash
cd backend
python -m venv venv
venv\Scripts\activate  # on Windows
pip install -r requirements.txt

# Download spaCy model (only once)
python -m spacy download en_core_web_sm

# Start API
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
Frontend
bash
cd frontend
npm install
npm start
Why this project
This project is designed to showcase:

Production‑style engineering: clear separation of frontend/backend, typed API models, and Dockerized deployment.

Applied AI skills: practical use of spaCy, SBERT, and similarity metrics on a real‑world hiring problem.

Readiness for large‑scale systems: the architecture can be extended with authentication, logging, and cloud deployment (e.g., Azure Container Apps or Web Apps).
