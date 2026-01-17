A = input().split()
B = input()
count = 0

for i in range(len(A)):
  if A[i] != B and A[i].startswith(B):
    count += 1

print(count)