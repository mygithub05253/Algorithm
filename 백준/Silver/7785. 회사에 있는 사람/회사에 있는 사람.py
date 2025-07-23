import sys
input = sys.stdin.readline

n = int(input())
log = set()

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        log.add(name)
    else:
        log.discard(name)

for name in sorted(log, reverse=True):
    print(name)