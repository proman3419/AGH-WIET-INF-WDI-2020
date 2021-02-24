x = int(input())

n = 0
while True:
  A_n = n*n + n + 1
  if A_n > x:
    print('no')
    break
  if A_n % x == 0:
    print('yes')
    break
  n += 1
