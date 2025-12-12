# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy our python file from your laptop into the container
COPY . .

# The command to run when the container starts
CMD ["python", "app.py"]
