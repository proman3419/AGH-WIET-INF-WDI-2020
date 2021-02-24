A, n = map(int, input().split())
e = 0.1**6
x = 1
y = 10

while abs(y-x) > e:
  x, y = y, (1/n)*((n-1)*x + A/(x**(n-1)))

print(y)
