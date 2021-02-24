a, b, n = map(int, input().split())

print(a//b, end='.')
a %= b
while n > 0:
  a *= 10
  print(a//b, end='')
  a %= b
  n -= 1
