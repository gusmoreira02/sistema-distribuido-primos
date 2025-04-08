from mpi4py import MPI
import sys

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
LIMIT = 10000

if rank == 0:
    print(f"\n[Coordenação] Buscando primos até {LIMIT} com {size} processos...")

# Divisão dinâmica do trabalho
chunk = LIMIT // size
start = rank * chunk
end = LIMIT if rank == size-1 else (rank+1)*chunk

print(f"[Processo {rank}] Verificando de {start} até {end}...")
primos_locais = [n for n in range(rank, LIMIT, size) if is_prime(n)]

# Coleta global
primos_globais = comm.gather(primos_locais, root=0)

if rank == 0:
    resultado = []
    for subset in primos_globais:
        resultado.extend(subset)
    resultado.sort()
    
    print(f"\n[RESULTADO FINAL] {len(resultado)} primos encontrados:")
    print(resultado)