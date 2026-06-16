# Containerfile
# Build: podman build -t finance-tracker .
# Run:   podman run -d -p 5000:5000 --name finance-tracker finance-tracker

FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install dependencies first (cached layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into container
COPY . .

# Create writable data directory for SQLite
RUN mkdir -p /app/data && chmod 777 /app/data

# Expose Flask port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
