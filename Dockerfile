# Base image
FROM python:3.12-slim

# Environment
ENV PYTHONUNBUFFERED=1 LANG=C.UTF-8

# Working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Ollama
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://ollama.ai/install.sh | bash

# Copy app code and startup script
COPY . .
COPY start.sh .
RUN chmod +x start.sh

# Expose Streamlit port
EXPOSE 8501

# Start everything at container runtime
CMD ["./start.sh"]
