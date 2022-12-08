from numpy import Inf
import timeit
import time
import random

def createUnvisitedGraph(numberOfNodes):
    unvisited=[]
    for i in range(numberOfNodes):
        unvisited.append([i,[]])
    return unvisited

def addEdge(unvisited,edge,sourceNodeIdx):
    unvisited[sourceNodeIdx][1].append(edge)
    unvisited[edge[0]][1].append([sourceNodeIdx,edge[1]])
    return unvisited

def generateEdges(unvisited,multiplier=1):
    numberOfEdges = len(unvisited)*2*multiplier
    numberOfNodes = len(unvisited)
    t=-1
    w=-1
    for i in range(numberOfEdges):
        src=-1
        if i < numberOfNodes*2:
            #print(i, ((numberOfNodes) * 2)-1)
            if i > (((numberOfNodes) * 2)-1)/2:
                src = (((numberOfNodes) * 2)-1)-i

            else:
                src=i
        else:
            src =  random.randint(0,numberOfNodes-1)
        t=src
        while t==src:
            t=random.randint(0,numberOfNodes-1)
        w = random.randint(1,20)
        unvisited=addEdge(unvisited,[t,w],src)
    return unvisited



def naive_dijkstras(graph, root):
    n = len(graph)
    # initialize distance list as all infinities
    dist = [Inf for _ in range(n)]
    # set the distance for the root to be 0
    dist[root] = 0
    # initialize list of visited nodes
    visited = [False for _ in range(n)]
    # loop through all the nodes
    for _ in range(n):
        # "start" our node as -1 (so we don't have a start/next node yet)
        u = -1
        # loop through all the nodes to check for visitation status
        for i in range(n):
            # if the node 'i' hasnt been visited and
            # we haven't processed it or the distance we have for it is less
            # than the distance we have to the "start" node
            if not visited[i] and(u== -1 or dist[i]<dist[u]):  # Odabire se sljedeći vrh koji ima najmanju udaljenost od selected vrha
                u=i
                # set the node as visited
        visited[u] = True
        # compare the distance to each node from the "start" node
        # to the distance we currently have on file for it
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
        # all the nodes have been visited or we can't reach this node
        if dist[u] == Inf:
            break
    return dist


def naive_dijkstras(graph, root):
    n = len(graph)
    dist = [Inf for _ in range(n)]
    dist[root] = 0
    visited = [False for _ in range(n)]
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and(u== -1 or dist[i]<dist[u]):
                u=i
        visited[u] = True
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
        if dist[u] == Inf:
            break
    return dist


# create our graph using an adjacency list representation
# each "node" in our list should be a node name and a distance
#(node,distance)
graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]
}

n = 2000
m = 2
unvisited2=createUnvisitedGraph(n)
unvisited2=generateEdges(unvisited2,m)
test={}
i=0
for item in unvisited2:
    test[i]=item[1]
    i=i+1
t0=time.time()
d=naive_dijkstras(test,0)
print("Sekvencjalni Dijkstra; vrhova:",n,", bridova:",n*2*m,", vrijeme:",time.time()-t0,)

