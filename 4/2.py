from random import randint


def odd_row(T, N):
  for i in range(N):
    for j in range(N):
      while T[i][j] > 0:
        if not (T[i][j]%10)%2:
          break
        T[i][j] //= 10
      else:
        break
    else:
      return False
  return True


N = int(input())
T = []
for i in range(N):
  T.append([randint(1, 10) for j in range(N)])

for r in T:
  print(r)
print(odd_row(T, N))
