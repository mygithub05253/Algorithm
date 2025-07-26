import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == '1':  # push
        stack.append(int(cmd[1]))
    elif cmd[0] == '2':  # pop
        print(stack.pop() if stack else -1)
    elif cmd[0] == '3':  # size
        print(len(stack))
    elif cmd[0] == '4':  # empty
        print(0 if stack else 1)
    elif cmd[0] == '5':  # top
        print(stack[-1] if stack else -1)