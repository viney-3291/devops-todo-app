# Start with a Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (for faster builds)
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the app code
COPY . .

# Tell Docker the app runs on port 5000
EXPOSE 5000

# Command to run the app
CMD ["python3", "app.py"]