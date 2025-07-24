from queue import Queue

N, K = map(int, input().split())

visited = [-1 for _ in range(100001)]

Q = Queue()
Q.put(N)
visited[N] = 0

while not Q.empty():
  current = Q.get()
  
  next = current * 2
  if 0 <= next <= 100000:
    if visited[next] == -1 and visited[next] < visited[current]:
      Q.put(next)
      visited[next] = visited[current]
  
  for move in [-1, 1]:
    next = current + move
    
    if 0 <= next <= 100000:
      if visited[next] == -1:
        Q.put(next)
        visited[next] = visited[current] + 1

print(visited[K])