vps = input()

stack = []
error = 0
tmp = 1
answer = 0

for i in range(len(vps)):
  data = vps[i]
  
  if data == "(":
    tmp *= 2
    stack.append(data)
  elif data == "[":
    tmp *= 3
    stack.append(data)
  elif data == ")":
    if not stack or stack[-1] != "(":
      answer = 0
      break
    if vps[i - 1] == "(":
      answer += tmp
    tmp //= 2
    stack.pop()
  elif data == "]":
    if not stack or stack[-1] != "[":
      answer = 0
      break
    if vps[i - 1] == "[":
      answer += tmp
    tmp //= 3
    stack.pop()   

if stack:
  print(0)
else:
  print(answer)