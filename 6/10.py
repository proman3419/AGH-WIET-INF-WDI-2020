from random import randint


def func(t, n):
  if n == 2:
    return t[0][0]*t[1][1] - t[1][0]*t[0][1]

  _n = n - 1
  res = 0
  for i in range(n):
    _t = t[1:]

    for j in range(_n):
      _t[j] = _t[j][:i] + _t[j][i+1:]

    res += (-1)**(i%2) * t[0][i] * func(_t, _n)

  return res


N = int(input())
rr = (1, 2)
t = [[randint(rr[0], rr[1]) for _ in range(N)] for _ in range(N)]
print(func(t, len(t)))
