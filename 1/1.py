_max = 10**6
a = b = 1

print('{}\n{}'.format(a, b))
while a+b < _max:
  a, b = b, a+b
  print(b)
