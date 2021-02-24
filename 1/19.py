def fact(n):
  if n == 0:
    return 1
  return n*fact(n-1)


e = 0.1**6
x1 = x2 = 1
i = 2
_sum = 2
while True:
  x1, x2 = x2, 1/fact(i)
  if x1 - x2 < e:
    break
  _sum += x2
  i += 1

print(_sum)
