import math

x1 = 1
x2 = multiplier = math.sqrt(0.5)
e = 0.1**6

while abs(x1-x2) > e:
  multiplier = math.sqrt(0.5+0.5*multiplier)
  x1, x2 = x2, x2*multiplier

print(2/x2)
