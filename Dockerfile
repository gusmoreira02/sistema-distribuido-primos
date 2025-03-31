FROM python:3.11-slim

# Instala dependências do MPI e Python
RUN apt-get update && \
    apt-get install -y openmpi-bin libopenmpi-dev && \
    pip install --no-cache-dir mpi4py

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Comando padrão (vai ser sobrescrito pelo docker-compose)
CMD ["python3", "primos_mpi.py"]
