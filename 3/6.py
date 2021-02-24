from random import randint


N = int(input())
a = [0]*N

for i in range(N):
  a[i] = randint(1, 1000)
  print(a[i], end=' ')
print()

for i in range(N):
  odd_flag = False
  while a[i] > 0:
    if (a[i] % 10) % 2 == 1:
      odd_flag = True
      break
    a[i] //= 10
    
  if not odd_flag:
    print('no')
    break
else:
  print('yes')
