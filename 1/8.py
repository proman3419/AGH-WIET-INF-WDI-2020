n = int(input())
i = 2

if n <= 1:
  print('not prime')
else:
  while i*i <= n:
    if n % i == 0:
      print('not prime')
      break
    i += 1

  if i*i > n:
    print('prime') 
