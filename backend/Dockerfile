FROM python:3.10-slim

WORKDIR /app

# Install system dependencies (gcc/g++ for scientific/ML libs)
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies (backend/requirements.txt)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install spaCy English model via wheel
RUN pip install --no-cache-dir \
  https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl

# Copy backend app code
COPY app ./app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
