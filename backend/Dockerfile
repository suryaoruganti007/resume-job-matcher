FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

# Copy requirements first for caching
COPY backend/requirements.txt .

# Install Python deps (this image has gcc + all build tools)
RUN pip install --no-cache-dir -r requirements.txt

# Install spaCy model
RUN python -m spacy download en_core_web_sm

# Copy app code
COPY backend/app ./app

EXPOSE $PORT
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "$PORT"]
