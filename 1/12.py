def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)


x, y, z = map(int, input().split())
print(gcd(gcd(x, y), z))
