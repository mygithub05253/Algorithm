# 행렬의 크기 N과 M 입력 받기
N, M = map(int, input().split())

matrix1 = []
for i in range(N):
  matrix1.append(list(map(int, input().split())))

matrix2 = []
for i in range(N):
  matrix2.append(list(map(int, input().split())))

# 두 개의 행렬의 합 출력
for i in range(N):
  for j in range(M):
    print(matrix1[i][j] + matrix2[i][j], end=" ")
  print()