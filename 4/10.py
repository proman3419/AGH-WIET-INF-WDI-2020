from random import randint


def zeros_in_col_row(T, N):
  for i in range(N):
    row = col = False
    for j in range(N):
      if T[i][j] == 0:
        row = True
      if T[j][i] == 0:
        col = True
      if row and col:
        break
    else:
      return False

  return True


N = int(input())
T = []
for i in range(N):
  T.append(sorted([randint(-10, 10) for j in range(N)]))

for r in T:
  print(r)
print(zeros_in_col_row(T, N))
