elems_cnt = 10
a = [0]*elems_cnt

while True:
  n = int(input())
  if n == 0:
    break

  i = 0
  while i <= elems_cnt and n <= a[i]:
    i += 1
  
  for j in range(elems_cnt-1, i-1, -1):
    a[j] = a[j-1]
  a[i] = n

for i in range(elems_cnt):
  if a[i] != 0:
    print(a[i], end=' ')
print()
