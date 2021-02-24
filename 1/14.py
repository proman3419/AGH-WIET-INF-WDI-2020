import math


def fact(x):
  res = 1
  for i in range(1, x+1):
    res *= i
  return res


# change x here (it's easier to import math.pi)
x_2, x_1, x = -1, 0, math.pi/4
e = 0.1**6
n = 0
_sum = 0

while abs(x_1-x_2) > e:
  x_1, x_2 = x_2, (-1)**n*x**(2*n)/fact(2*n)
  _sum += x_2
  n += 1

print(_sum)
