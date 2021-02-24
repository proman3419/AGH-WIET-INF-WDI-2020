def create():
  l, m = map(int, input().split())
  return (l, m)


def output(n):
  print(f'{n[0]}/{n[1]}')


def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)


def lcm(a, b):
  return a*b//gcd(a, b)


def add(a, b):
  _lcm = lcm(a[1], b[1])
  return (a[0]*_lcm//a[1] + b[0]*_lcm//b[1], _lcm)


def sub(a, b):
  _lcm = lcm(a[1], b[1])
  return (a[0]*_lcm//a[1] - b[0]*_lcm//b[1], _lcm)


def multiply(a, b):
  return (a[0]*b[0], a[1]*b[1])


def div(a, b):
  return (a[0]*b[1], a[1]*b[0])


def simplify(a):
  _gcd = gcd(a[0], a[1])
  return (a[0]//_gcd, a[1]//_gcd)


a = create()
b = create()
output(add(a, b))
output(sub(a, b))
output(multiply(a, b))
output(div(a, b))
output(simplify(a))
