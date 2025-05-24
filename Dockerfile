FROM python:3.12-slim

RUN apt-get update && apt-get install -y wireless-tools gpsd gpsd-clients && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY data/ ./data

WORKDIR /app/src

CMD ["python", "scan_wifi.py"]

