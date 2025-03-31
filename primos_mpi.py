from mpi4py import MPI

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Configuração do MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Verifica se há pelo menos 2 processos
if size < 2:
    if rank == 0:
        print("❌ Erro: O programa precisa de pelo menos 2 processos (1 gerente + 1 executor).")
    exit()

# Limite superior para buscar primos
LIMIT = 10000

# Processo gerente
if rank == 0:
    chunk_size = LIMIT // (size - 1)
    print(f"[Gerente] Enviando tarefas para {size - 1} executores...")

    # Enviar faixas para cada executor
    for i in range(1, size):
        start = (i - 1) * chunk_size
        end = LIMIT if i == size - 1 else i * chunk_size
        comm.send((start, end), dest=i)

    # Receber primos de todos os executores
    all_primes = []
    for i in range(1, size):
        local_primes = comm.recv(source=i)
        all_primes.extend(local_primes)

    # Ordenar e mostrar resultado
    all_primes.sort()
    print(f"\n[Gerente] Primos encontrados até {LIMIT}:")
    print(all_primes)

# Processos executores
else:
    start, end = comm.recv(source=0)
    print(f"[Executor {rank}] Buscando primos de {start} até {end}...")
    local_primes = [n for n in range(start, end) if is_prime(n)]
    comm.send(local_primes, dest=0)
