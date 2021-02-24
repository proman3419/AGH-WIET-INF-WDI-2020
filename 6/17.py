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


def cnt_built_primes(a, b, c=0):
  if a == b == 0:
    if is_prime(c):
      return 1
    return 0

  r1 = r2 = 0
  if a > 0:
    _len_a = int(log10(a))
    r1 = cnt_built_primes(a%10**_len_a, b, c*10+a//10**_len_a)
  if b > 0:
    _len_b = int(log10(b))
    r2 = cnt_built_primes(a, b%10**_len_b, c*10+b//10**_len_b)

  return r1 + r2         


a, b = map(int, input().split())
print(cnt_built_primes(a, b))
