n = int(input())
prev = n%10
n //= 10

while n > 0:
  curr = n%10
  if curr >= prev:
    print('no')
    break
  n //= 10
  prev = curr
else:
  print('yes')
