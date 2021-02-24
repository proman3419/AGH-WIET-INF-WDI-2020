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


def func(n, _len, rem_id):
  if _len == 1:
    return

  n = (n-n%(10**rem_id))//10 + n%(10**(rem_id-1))

  if is_prime(n):
    res.add(n)
  for i in range(1, _len+1):
    func(n, _len-1, i)


n = int(input())
_len = int(log10(n)) + 1
res = set()
for i in range(1, _len):
  func(n, _len-1, i)

for e in res:
  print(e)
