n = int(input())

a = b = 1
while b <= n:
  _a = _b = 1
  while _b <= b:
    if n/b == _b:
      print(b, _b)
      exit()
    _a, _b = _b, _a+_b
  a, b = b, a+b

print('no')
