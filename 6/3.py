from random import randint


def func(row, col, cost_total):
  if row == 8: return cost_total
  if col < 0 or col > 7: return 10**100

  r1 = func(row+1, col-1, cost_total+T[row][col])
  r2 = func(row+1, col, cost_total+T[row][col])
  r3 = func(row+1, col+1, cost_total+T[row][col])

  return min(r1, r2, r3)


k = int(input())
rr = (1, 8)
T = [[randint(rr[0], rr[1]) for _ in range(8)] for _ in range(8)]

for r in T:
  print(r)
print(func(0, k, 0))
