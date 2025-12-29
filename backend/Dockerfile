FROM python:3.11-slim  # Use 3.11 (more stable wheels)

WORKDIR /app

# Minimal deps - wheels only
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && python -m spacy download en_core_web_sm

COPY . .
EXPOSE $PORT
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "$PORT"]
