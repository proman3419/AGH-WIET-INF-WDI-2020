n = int(input())
last_digit = n % 10
n //= 10

while n > 0:
  if n % 10 == last_digit:
    print('no')
    break
  n //= 10
else:
  print('yes')
