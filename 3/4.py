def divide_array(_a, d):
  i = 0
  res = [0]*(precision+1)

  while i < precision:
    _a[i] *= 10
    res[i+1] = _a[i]//d
    _a[i+1] += _a[i]%d
    i += 1

  return res


def sum_arrays(_a, b):
  for i in range(precision, -1, -1):
    _a[i] += b[i]
    if _a[i] >= 10:
      _a[i-1] += _a[i]//10
      _a[i] %= 10


N = int(input())
precision = max(10*1, N)
a = [0]*(precision+1)
a[0] = 1
e = [0]*(precision+1)
e[0] = 2

for i in range(2, 1000):
  a = divide_array(a, i)
  sum_arrays(e, a)

print(e[0], end='.')
for i in range(1, N+1):
  print(e[i], end='')
