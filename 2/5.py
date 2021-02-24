n = int(input())
mod = 7

_n = n
digits = 0
while _n > 0:
  n = n*10 + _n%10
  _n //= 10
  digits += 1
n %= 10**digits

cnt = 0
for i in range(1, 2**digits):
  candidate = 0
  _n = n

  while i > 0:
    if i % 2:
      candidate = candidate*10 + _n%10
    _n //= 10
    i //= 2

  if candidate % mod == 0:
    cnt += 1

print(cnt)
