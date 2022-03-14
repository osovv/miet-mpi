from mpi4py import MPI


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    counter = 0
    while True:
        value, _ = comm.recv()
        counter += 1
        if value == -1:
            print(f'Master stopped. Counter: {counter}.')
            exit(0)
else:
    for value in range(1000, -2, -1):
        comm.send((value, rank), dest=0)
    print(
        f'Slave #{rank} stopped.')
