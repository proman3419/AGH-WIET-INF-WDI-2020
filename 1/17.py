a, b = map(int, input().split())
c = a+b
e = 0.1**6

while abs(a/b-b/c) > e:
  a = b
  b, c = c, b+c

print(b/c)
