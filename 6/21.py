from random import randint


def subset_with_sum(T, k):
  row = 0
  visited_cols = [False]*8
  flag = [False]

  def rec(T, k, visited_cols, row=0, _sum=0):
    if _sum == k:
      flag[0] = True
      return
    if _sum > k or row == 8: return
    
    for i in range(8):
      if flag[0]: return
      if not visited_cols[i]:
        _visited_cols = visited_cols[:]
        _visited_cols[i] = True
        rec(T, k, _visited_cols, row+1, _sum+T[row][i])


  rec(T, k, visited_cols)

  return flag[0]


k = int(input())
rr = (0, 1)
T = [[randint(rr[0], rr[1]) for _ in range(8)] for _ in range(8)]

for r in T:
  print(r)
print(subset_with_sum(T, k))
