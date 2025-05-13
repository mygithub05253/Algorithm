import sys

if __name__ == '__main__':
  T = int(sys.stdin.readline())
  result = []
  for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    result.append(A + B)
  for i in result:
    print(i)  