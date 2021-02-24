N = int(input())

cnt = 0
for i in range(1, N+1):
  _i = i
  while not i % 2:
    i //= 2
  while not i % 3:
    i //= 3
  while not i % 5:
    i //= 5
  if i == 1:
    cnt += 1

print(cnt)
