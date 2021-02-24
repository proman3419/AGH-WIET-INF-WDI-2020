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


def count_digits(n, i, A=0, B=0):
  if i == 0:
    return (A, B)
  if n % 2 == 1: A += 1
  else: B += 1

  return count_digits(n//2, i-1, A, B)


def possible_numbers(A, B, n=0):
  cnt = 0
  target = 2**(A+B)
  for i in range(target//2, target):
    _A, _B = count_digits(i, A+B)
    if _A == A and _B == B and not is_prime(i):
      cnt += 1

  return cnt


A, B = map(int, input().split())
print(possible_numbers(A, B))
