def is_prime(n):
  i = 3
  while i*i < n:
    if n % i == 0:
      return False
    i += 2
  return True


_sum = 1
i = 1
while _sum*2**i < 10**6:
  _sum += 2**i
  if is_prime(_sum):
    print(_sum*2**i)
  i += 1
