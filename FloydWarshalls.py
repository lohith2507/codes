import sys
def floydWarshall(graph,V):
    D = [[0 for _ in range(V)] for _ in range(V)]  # Distance matrix
    P = [[0 for _ in range(V)] for _ in range(V)]  # Path matrix
    # Initialize distance and path matrices
    for i in range(V):
        for j in range(V):
            D[i][j] = graph[i][j]
            if i == j or graph[i][j] == sys.maxsize:
                P[i][j] = -1  # No path
            else:
                P[i][j] = i
    # Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if D[i][k] != sys.maxsize and D[k][j] != sys.maxsize and D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = P[k][j]
    # Print distance matrix
    print("Distance Matrix D:")
    for i in range(V):
        for j in range(V):
            if D[i][j] == sys.maxsize:
                print("INF\t", end="")
            else:
                print(f"{D[i][j]}\t", end="")
        print()
    # Print path matrix 
    print("\nPath Matrix P:")
    for i in range(V):
        for j in range(V):
            print(f"{P[i][j]+1}\t", end="")
        print()
    return P
def constructPaths(P):
    num_vertices = len(P)
    shortest_paths_graph = [[] for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            if P[i][j] is not None:
                shortest_paths_graph[i].append((j, P[i][j]))
    return shortest_paths_graph

I = 9999
G1 = [[0, 1, I, 1, 5],
    [9, 0, 3, 2, I],
    [I, I, 0, 4, I],
    [I, I, 2, 0, 3],
    [3, I, I, I, 0]]
G2 = [[0 ,4, 5],
    [2, 0 , I],
    [I, -3, 0]]
P1 = floydWarshall(G1,len(G1))
shortest_paths_graph1 = constructPaths(P1)
print("\nShortest Paths Graph:")
for vertex, paths in enumerate(shortest_paths_graph1):
    for target, predecessor in paths:
        print(f"v{vertex} -> v{target}")
P2 = floydWarshall(G2, len(G2))
shortest_paths_graph2 = constructPaths(P2)
print("\nShortest Paths Graph:")
for vertex, paths in enumerate(shortest_paths_graph2):
    for target, predecessor in paths:
        print(f"v{vertex} -> v{target}")


