version: "3"

services:
  backend:
    build: .
    container_name: finance-tracker_backend_1
    ports:
      - "5000:5000"
    volumes:
      - ./data:/app/data
    restart: unless-stopped
