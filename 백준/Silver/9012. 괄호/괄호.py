T = int(input())

for _ in range(T):
  vps = input()
  
  stack = []
  check = False
  
  for data in vps:
    if data == "(":
      stack.append(data)
    else:
      if len(stack) == 0:
        check = True
        break
      else:
        stack.pop() 
  
  if len(stack) == 0 and check == False:
    print("YES")
  else:
    print("NO")