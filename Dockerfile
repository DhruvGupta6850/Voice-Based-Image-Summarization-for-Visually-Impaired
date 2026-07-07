FROM python:3.11-slim

WORKDIR /app

# Install system libraries required by OpenCV, Pillow, EasyOCR
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better Docker caching)
COPY requirements.txt .

# Upgrade pip and Install Python packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Create required folders
RUN mkdir -p static/uploads static/audio

# Hugging Face Spaces uses port 7860
EXPOSE 7860

ENV PORT=7860
ENV PYTHONUNBUFFERED=1
ENV HF_HOME=/tmp/huggingface

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:7860", "--workers", "1", "--timeout", "300"]