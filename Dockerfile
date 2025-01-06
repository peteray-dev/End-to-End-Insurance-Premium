# FROM python:3.8.5-slim-buster

# WORKDIR /app

# COPY . /app

# RUN pip install -r requirements.txt

# CMD ["python3", "app.py"]


FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Install system dependencies for LightGBM
RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    cmake \
    libgomp1

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
