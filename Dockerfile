# Use a small Python base
FROM python:3.12-slim

# Make Python friendlier in containers
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Workdir inside the container
WORKDIR /app

# System packages (tzdata for timezones; libpq for Postgres client libs)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 tzdata \
 && rm -rf /var/lib/apt/lists/*

# Install Python deps first (better layer caching)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your project
COPY . .

# Port your Django app listens on (container side)
EXPOSE 8000

# Production default (Compose overrides this in dev)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
