n = int(input())

N = 0
_n = n
while _n > 0:
  _n //= 10
  N += 1

_n = n
while _n > 0:
  n -= (_n%10)**N
  _n //= 10

print('yes') if n == 0 else print('no')
