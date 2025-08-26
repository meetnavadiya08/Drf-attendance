FROM python:3.12-slim

# Set workdir
WORKDIR /app

# Install dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
