N = int(input())
a = [True]*N

i = 2
while i*i < N:
  if a[i]:
    for j in range(i*i, N, i):
      a[j] = False
  i += 1

for i in range(2, N):
  if a[i]:
    print(i)
