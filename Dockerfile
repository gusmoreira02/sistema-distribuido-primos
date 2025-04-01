FROM python:3.11-slim

# Instalar dependências necessárias
RUN apt-get update && apt-get install -y openmpi-bin libopenmpi-dev \
    && pip install --no-cache-dir mpi4py

# Defina o diretório de trabalho
WORKDIR /app

# Copiar o código para o diretório do container
COPY . .

# Comando para executar o script
CMD ["python3", "primos_mpi.py"]
