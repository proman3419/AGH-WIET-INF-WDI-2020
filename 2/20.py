a, b = map(int, input().split())

base = 2
while base <= 16:
  _a = a
  while _a > 0:
    digit = _a % base
    _b = b
    while _b > 0:
      _digit = _b % base
      if digit == _digit:
        _a = -1
        break
      _b //= base
    _a //= base

  if _a == 0:
    print(base)
    base = 999
    break

  base += 1

if base == 17:
  print('no such base in range [2, 16]')
