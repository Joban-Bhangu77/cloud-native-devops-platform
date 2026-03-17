# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy your Product Service app into the container
COPY app/product-service/ .

# Install dependencies
RUN pip install --no-cache-dir Flask==2.3.2

# Expose port 5000
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]