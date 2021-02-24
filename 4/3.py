from random import randint


def even_row(T, N):
  i = 0
  while i < N:
    for j in range(N):
      while T[i][j] > 0:
        if not (T[i][j]%10)%2:
          break
        T[i][j] //= 10
      else:
        i += 1
        break
    else:
      return True
  return False


N = int(input())
T = []
for i in range(N):
  T.append([randint(1, 10) for j in range(N)])

for r in T:
  print(r)
print(even_row(T, N))
