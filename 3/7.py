from random import randint


N = int(input())
a = [0]*N

for i in range(N):
  a[i] = randint(1, 1000)
  print(a[i], end=' ')
print()

for i in range(N):
  while a[i] > 0:
    if (a[i] % 10) % 2 == 0:
      print('no')
      exit()
    a[i] //= 10

print('yes')
