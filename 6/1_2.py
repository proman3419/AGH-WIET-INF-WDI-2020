from math import log10


def is_prime(n):
  if n < 2: return False
  if n == 2: return True
  if n % 2 == 0: return False
  
  i = 3
  while i*i <= n:
    if n % i == 0:
      return False
    i += 2

  return True


def func(n, k, _len):
  if n == 0:
    if k >= 10 and is_prime(k):
      res.add(k)
    return

  func(n//10, k+(10**_len)*(n%10), _len+1)
  func(n//10, k, _len)


n = int(input())
n = 12341232134433
res = set()

func(n, 0, 0)

for e in res:
  print(e)
