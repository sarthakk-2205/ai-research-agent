
FROM python:3.12-slim

WORKDIR /app

# Keep Python output visible in Docker logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install project dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# API and Streamlit ports
EXPOSE 8000 8501
