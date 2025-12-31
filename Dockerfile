# Base Image
FROM python:3.12-slim

# Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=gcp_study_plan.settings

# Work Directory
WORKDIR /app

# Install System Dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python Dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copy Project
COPY . /app/

# Entrypoint
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# Expose Port
EXPOSE 8000

# Run
ENTRYPOINT ["/app/entrypoint.sh"]
