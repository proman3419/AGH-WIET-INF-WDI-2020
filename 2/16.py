def sum_digits(n):
  _sum = 0
  while n > 0:
    _sum += n%10
    n //= 10
  return _sum


_max = 10**3

for i in range(1, _max):
  _i = i
  j = 2
  _sum = 0
  while j < _i:
    while i % j == 0:
      i //= j
      _sum += sum_digits(j)
    j += 1

  if _sum == sum_digits(_i):
    print(_i)
