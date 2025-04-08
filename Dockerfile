FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y \
    openmpi-bin \
    libopenmpi-dev \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sleep", "infinity"]