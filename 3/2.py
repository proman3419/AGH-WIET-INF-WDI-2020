from math import log10


a, b = map(int, input().split())
digits = [0]*10

while a > 0:
  digits[a%10] += 1
  a //= 10

while b > 0:
  digits[b%10] -= 1
  b //= 10

for i in range(10):
  if digits[i] != 0:
    print('no')
    break
else:
  print('yes')
