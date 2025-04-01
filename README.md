# 🔢 Sistema Distribuído de Busca de Números Primos com MPI

Este projeto demonstra a aplicação de um sistema distribuído usando o framework **MPI** para calcular números primos de forma paralela e distribuída entre múltiplos processos, simulando execução em cluster ou grid.

## ✅ Requisitos Atendidos

✔️ Alimenta um vetor contendo apenas números primos  
✔️ Vetor contém todos os primos até um valor máximo (LIMIT)  
✔️ Vetor final é ordenado do menor ao maior  
✔️ Utiliza **MPI** para distribuir a tarefa entre múltiplos processos  
✔️ Simula múltiplos computadores via Docker + MPI  
✔️ Pronto para rodar em Linux, Docker 

## 📦 Clonar o projeto

```bash
git clone https://github.com/gusmoreira02/sistema-distribuido-primos.git
cd sistema-distribuido-primos
```

## 🐳 Como Executar com Docker 

### 🧱 Requisitos

- Docker 
- Docker Compose

### 🔧 Build e execução

```bash
docker-compose build
docker-compose up
```

## 💻 Executar manualmente (sem Docker)

### 1. Instalar dependências (Linux)

```bash
sudo apt update
sudo apt install -y python3 python3-pip openmpi-bin libopenmpi-dev
pip install mpi4py
```

> Ou use virtualenv:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Executar o código com MPI

```bash
mpirun -n 4 python3 primos_mpi.py
```

## 🌐 Execução em Rede (Com 2 VMs)

Se desejar rodar entre duas VMs na mesma rede (192.168.50.0/24), utilize o parâmetro `--host` com IPs das máquinas:

### Exemplo:

```bash
mpirun -np 4 --host 192.168.50.10,192.168.50.11 python3 primos_mpi.py
```

Garanta que:
- As máquinas estejam com OpenMPI instalado
- A comunicação SSH entre elas esteja liberada

## 📁 Estrutura dos arquivos

- `primos_mpi.py`: código principal
- `Dockerfile`: ambiente de execução com Python + MPI
- `docker-compose.yml`: orquestra execução com múltiplos processos
- `requirements.txt`: dependências Python
- `.gitignore`: ignora a pasta `venv/` no Git

## 👨‍🏫 Informações do Aluno

**Nome:** Gustavo Moreira  
**Matricula:** 7725736  
**Curso:** Engenharia da computação

## ✅ Testado em:

- Ubuntu 22.04 (WSL 2)
- Docker 26.1.3
- Python 3.11
- OpenMPI
- mpi4py 4.0.3
