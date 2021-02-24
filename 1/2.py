curr_year = 2020


def fib(a_in, b_in):
  a = a_in
  b = b_in
  while b < curr_year:
    a, b = b, a+b
    if b == curr_year:
      print(a_in, b_in)
      return True
  return False


a = b = 1
_sum = 2
while True: 
  for i in range(_sum//2+1):
    a = i
    b = _sum - i
    if fib(a, b) or fib(b, a):
      exit()
  _sum += 1
