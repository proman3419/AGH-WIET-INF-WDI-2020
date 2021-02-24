from random import randint


def max_quotient_ids(T, N):
  _min_row_sum = 10**100
  _max_col_sum = -1
  ids = [-1, -1]
  for i in range(N):
    row_sum = 0
    col_sum = 0
    for j in range(N):
      row_sum += T[i][j]
      col_sum += T[j][i]

    if row_sum < _min_row_sum:
      _min_row_sum = row_sum
      ids[1] = i

    if col_sum > _max_col_sum:
      _max_col_sum = col_sum 
      ids[0] = i

  return ids


N = int(input())
T = []
for i in range(N):
  T.append([randint(1, 10) for j in range(N)])

for r in T:
  print(r)
print(max_quotient_ids(T, N))
