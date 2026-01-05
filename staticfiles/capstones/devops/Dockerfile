# Use official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install flask

# Expose port (Cloud Run uses 8080 by default)
ENV PORT 8080

# Run the app
CMD ["python", "app.py"]
