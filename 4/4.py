from random import randint


def max_quotient_ids(T, N):
  cols_sums = [0]*N
  for i in range(N):
    for j in range(N):
      cols_sums[i] += T[j][i]

  rows_sums = [0]*N
  for i in range(N):
    for j in range(N):
      rows_sums[i] += T[i][j]

  max_ids = [0, 0]
  max_quotient = 0
  for i in range(N):
    for j in range(N):
      curr_quotient = cols_sums[i]/rows_sums[j]
      if curr_quotient > max_quotient:
        max_quotient = curr_quotient
        max_ids = [i, j]

  return max_ids


N = int(input())
T = []
for i in range(N):
  T.append([randint(1, 10) for j in range(N)])

for r in T:
  print(r)
print(max_quotient_ids(T, N))
