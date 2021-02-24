a = 0
b = 10
e = 0.000001
t = 2020


def f(x):
  return x**x - 2020


while True:
  s = (a + b)/2
  if abs(f(s)) <= e:
    break
  if f(s)*f(a) < 0:
    b = s
  else:
    a = s

print(s)
