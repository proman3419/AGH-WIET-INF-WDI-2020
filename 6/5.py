from random import randint


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


def func(i):
  if i == N: return True

  _sum = 0
  for j in range(i, min(N, i+30)):
    _sum = 2*_sum + T[j]
    if is_prime(_sum) and func(j+1):
      return True

  return False


N = int(input())
T = [randint(0, 1) for _ in range(N)]
print(T)
print(func(0))
