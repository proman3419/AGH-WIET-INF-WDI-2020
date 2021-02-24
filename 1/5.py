A = int(input())
e = 0.1**6
x = 1
y = 10

while abs(y-x) > e:
  x, y = y, 0.5*(x + A/x)

print(y)
