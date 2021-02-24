n = int(input())
cnt = 0

i2 = 1
while i2 <= n:
  i3 = i2
  while i3 <= n:
    i5 = i3
    while i5 <= n:
      cnt += 1
      i5 *= 5
    i3 *= 3
  i2 *= 2

print(cnt)
