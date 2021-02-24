def func(i, _sum, _sum_id, _len):
  if i == N: 
    if _sum == _sum_id and _len != 0:
      return (_len, _sum)
    else:
      return (N+1, -1)

  r1 = func(i+1, _sum, _sum_id, _len)
  r2 = func(i+1, _sum+T[i], _sum_id+i, _len+1)
  if r1[0] < r2[0]:
    return r1
  else:
    return r2


#T = [1, 7, 3, 5, 11, 2]
T = [2323, 12, 3, 1, 5, 112, 11, 27]
N = len(T)
print(func(0, 0, 0, 0))
