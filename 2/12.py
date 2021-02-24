n = int(input())

i = 0
_n = n
while _n > 0:
  _n //= 10
  i += 1

while n > 0:
  if n % 10 == i:
    print(i)
    break
  n //= 10
else:
  print('no')
