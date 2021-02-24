x = int(input())
A_n = 2

while True:
  if A_n > x:
    print('no')
    break
  if x % A_n == 0:
    print('yes')
    break
  A_n = 3*A_n + 1
