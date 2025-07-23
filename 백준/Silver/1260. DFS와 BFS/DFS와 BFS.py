def DFS(vtx, adj, s, visited):
  print(vtx[s - 1], end=" ")
  visited[s] = True
  for v in range(1, len(vtx) + 1):
    if adj[s][v] != 0:
      if visited[v] == False:
        DFS(vtx, adj, v, visited)

from queue import Queue

def BFS_AL(vtx, aList, s):
  n = len(vtx)
  visited = [False] * (len(vtx) + 1)
  Q = Queue()
  Q.put(s)
  visited[s] = True
  while not Q.empty():
    s = Q.get()
    print(vtx[s - 1], end=" ")
    for v in aList[s]:
      if visited[v] == False:
        Q.put(v)
        visited[v] = True

N, M, V = map(int, input().split())

vtx = [i for i in range(1, N + 1)]
edge = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().split())
  edge[a][b] = 1
  edge[b][a] = 1

aList = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if edge[i][j] == 1:
            aList[i].append(j)

for i in range(1, N + 1):
    aList[i].sort()

DFS(vtx, edge, V, [False] * (N + 1))
print()
BFS_AL(vtx, aList, V)