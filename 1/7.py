n = int(input())
a = b = 1
fib = {a: True}

while a + b <= n:
  a, b = b, a+b
  fib[b] = True

for k in fib:
  try:
    if fib[n//k]:
      print(k, n//k)
      exit()
  except KeyError:
    pass

print('no')
