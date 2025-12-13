FROM python:3.9-slim

WORKDIR /app

# --- NEW STEPS ---
# Copy the ingredients list first
COPY requirements.txt .
# Install the ingredients (Flask)
RUN pip install -r requirements.txt
# -----------------

COPY . .

CMD ["python", "app.py"]
