K = int(input())

stack = []
sum = 0

for i in range(K):
  number = int(input())
  if number == 0:
    if not stack or stack[-1] != 0:
      sum -= stack.pop()
    else:
      stack.append(number)
      sum += number
  else:
    stack.append(number)
    sum += number
print(sum)