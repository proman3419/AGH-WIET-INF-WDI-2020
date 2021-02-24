def waga(n):
  i = 2
  cnt = 0
  while n > 1:
    if n % i == 0:
      cnt += 1
      while n % i == 0:
        n //= i
    i += 1

  return cnt


def func(i, sum1, sum2, sum3):
  if sum1 > _sum_rd or sum2 > _sum_rd or sum3 > _sum_rd: return False
  if i == N:
    if sum1 == sum2 == sum3: return True
    else: return False

  return func(i+1, sum1+T[i], sum2, sum3) or func(i+1, sum1, sum2+T[i], sum3) or func(i+1, sum1, sum2, sum3+T[i])


N = 6
T = [2, 3, 6, 2, 4, 1]
for i in range(N):
  T[i] = waga(T[i])

_sum = sum(T)
if _sum % 3 == 0:
  _sum_rd = _sum//3
  print(func(0, 0, 0, 0))
