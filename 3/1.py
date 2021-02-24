num_to_char = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def to_base(n, base):
  _n = n
  _len = 0
  while _n > 0:
    _n //= base
    _len += 1

  a = ['0']*_len

  i = 0
  while i < _len:
    rem = n%base
    if rem >= 10:
      a[i] = num_to_char[rem]
    else:
      a[i] = rem
    n //= base
    i += 1

  i -= 1

  print(f'{base}x', end='')
  while i >= 0:
    print(a[i], end='')
    i -= 1


n, base = map(int, input().split())
to_base(n, base)
