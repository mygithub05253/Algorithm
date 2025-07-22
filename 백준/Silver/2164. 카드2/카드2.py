from queue import Queue

N = int(input())

card = Queue()

for i in range(1, N + 1):
  card.put(i)

while card.qsize() > 1:
  card.get()
  number = card.get()
  card.put(number)

print(card.get())