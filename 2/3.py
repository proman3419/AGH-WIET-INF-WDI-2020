n = int(input())


def is_palindrome(n, base):
  _n = n
  max_i = 0
  while _n > 0:
    _n //= base
    max_i += 1

  flag = True
  for i in range(1, (max_i+1)//2):
    if n%base**(max_i-i+1)//base**(max_i-i) != n%base**i//base**(i-1):
      flag = False
      break

  print(base, end=': ')
  print('yes') if flag else print('no')


is_palindrome(n, 10)
is_palindrome(n, 2)
