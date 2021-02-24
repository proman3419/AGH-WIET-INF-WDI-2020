def gen_divisors_sum(n):
  _sum = 1
  i = 2
  while i*i < n:
    if n % i == 0:
      _sum += i + n//i
    i += 1
  if i*i == n:
    _sum += i

  return _sum


def gen_divisors_sum_range(a, b):
  d = {}
  for i in range(a, b):
    d[i] = gen_divisors_sum(i)

  return d


_max = 10**6
d = gen_divisors_sum_range(1, _max)
res = []
for k in d:
  try:
    if k == d[d[k]] and k != d[k]:
      res.append(sorted[k, d[k]])
  except KeyError:
    pass

res.sort()

for i in range(0, len(res), 2):
  print(res[i])
