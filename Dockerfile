FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -f requirements.txt 
COPY . .
CMD ["python", "app.py"]