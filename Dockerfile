FROM python:3.10-slim

# Update OS packages (reduce vulnerabilities)
RUN apt-get update && apt-get upgrade -y

WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip + setuptools (reduce Python CVEs)
RUN pip install --upgrade pip setuptools

# Install dependencies
RUN pip install -r requirements.txt

# Run your app (correct path based on your repo)
CMD ["python", "app/product-service/app.py"]
