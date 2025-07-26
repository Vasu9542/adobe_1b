FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y gcc g++ && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y gcc g++ && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python", "main.py"]
