from random import randint


def friendly_neighbours(T, N):
  pass


N = int(input())
T = []
for i in range(N):
  T.append(sorted([randint(-10, 10) for j in range(N)]))

for r in T:
  print(r)
print(friendly_neighbours(T, N))
