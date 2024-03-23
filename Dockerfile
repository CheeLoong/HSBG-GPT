# Use the official Python image from Docker Hub
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required by Playwright
RUN apt-get update && apt-get install -y \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libatspi2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libdrm2 \
    libxkbcommon0 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Copy the Python requirements file
COPY requirements.txt .

# Install Playwright and its dependencies
RUN pip install playwright==1.42.0
RUN playwright install

# Copy the Python script into the container
COPY playwright_demo.py .

# Run the Python script when the container starts
CMD ["python", "playwright_demo.py"]
