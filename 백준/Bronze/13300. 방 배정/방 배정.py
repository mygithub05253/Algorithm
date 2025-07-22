n, k = map(int, input().split())

student = [[0, 0] for _ in range(7)]

for _ in range(n):
  s, g = map(int, input().split())
  student[g][s] += 1

room = 0

for i in student:
  room += i[0] // k
  
  if i[0] % k:
    room += 1
  
  room += i[1] // k
  if i[1] % k:
    room += 1  

print(room)