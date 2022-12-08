from mpi4py import MPI
import timeit
import time
import numpy as np
import random
import sys
import math


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def singleSourcDijkstra(n, source, wgt, lengths):
    nlocal = int(math.floor(n / size))
    lminpair=[-1]*2
    gminpair=[-1]*2

    firstvtx = rank * nlocal;
    lastvtx = firstvtx + nlocal - 1;

    for k in range(nlocal):
        lengths[k]=int(wgt[source * nlocal + k])

    marker=[1]*nlocal
    if source >= firstvtx and source <= lastvtx:
        marker[source - firstvtx] = 0;

    for i in range(n-1):
        lminpair[0] = sys.maxsize
        lminpair[1] = -1
        for j in range(nlocal):
            if marker[j]==1 and lengths[j] < lminpair[0]:
                lminpair[0] = int(lengths[j])
                lminpair[1] = int(firstvtx + j)
        comm.barrier()
        gminpair=comm.allreduce(lminpair, op=MPI.MINLOC)

        udist = int(gminpair[0])
        u = int(gminpair[1])


        if(u == lminpair[1]):
            marker[u-firstvtx]=0

        for j in range(nlocal):
            if marker[j] and ((udist + wgt[u * nlocal + j]) < lengths[j]):
                lengths[j] = int(udist + wgt[u * nlocal + j])


    return lengths

"""
[0,1,0,0],
    [1,0,2,3],
    [0,2,0,0],
    [0,3,0,0]
"""

def ajasonMatrix(numberOfNodes):
    matrix=[]
    for i in range(numberOfNodes):
        matrix.append([sys.maxsize]*numberOfNodes)
    return matrix

def addEdge(matrix,u,v,w):
    matrix[u][v]=w
    matrix[v][u]=w
    return matrix

if rank==0:

    numberOfNodes = 2000
    numberOfEdges = 8000
    matrix = ajasonMatrix(numberOfNodes)
    for e in range(0, numberOfEdges):
        if (e < numberOfNodes - 1):
            matrix=addEdge(matrix,e, e + 1, random.randint(1, 20))
        else:
           matrix=addEdge(matrix,random.randint(0, numberOfNodes - 1), random.randint(0, numberOfNodes - 1),
                       random.randint(1, 20))
else:
    matrix = None

ajasonMatrix = comm.bcast(matrix, root=0)


"""
ajasonMatrix=[
    [sys.maxsize, 1, sys.maxsize, sys.maxsize],
    [1, sys.maxsize, 2, 3],
    [sys.maxsize, 2, sys.maxsize, sys.maxsize],
    [sys.maxsize, 3, sys.maxsize, sys.maxsize]
]
"""
N = len(ajasonMatrix)
npes = size
nlocal = int(math.floor(N / npes))
localWeight=[]
localDistance=[-1]*nlocal
source=0



sendbuf=np.zeros(N*N)
t0=timeit.timeit()
if rank==source:
    for k in range(npes):
        for i in range(N):
            for j in range(nlocal):
                sendbuf[k * N * nlocal + i * nlocal + j] = ajasonMatrix[i][k * nlocal + j];
    split = np.array_split(sendbuf, npes)
else:
    split=None
localWeight = comm.scatter(split, root=source)



distance=singleSourcDijkstra(N, source, localWeight, localDistance)

TotalDistance = comm.gather(distance, root=source)

if rank==source:
    print("Paralelno Dijkstra; vrhova:",numberOfNodes,", bridova:",numberOfEdges,"bridova, vrijeme:",timeit.timeit()-t0)

