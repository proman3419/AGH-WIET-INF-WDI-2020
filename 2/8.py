n = int(input())

if n <= 3:
  print(4)
else:
  a = b = 1
  while b < n:
    a, b = b, a+b

  print(n+1) if n+1 != b else print(n+2)
