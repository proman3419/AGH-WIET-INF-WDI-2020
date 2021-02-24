max_cnt = 0
max_i = 0

for i in range(2, 10**4+1):
  cnt = 0
  A = i
  while A != 1:
    A = (A%2)*(3*A+1)+(1-(A%2))*A/2
    cnt += 1

  if cnt > max_cnt:
    max_cnt = cnt
    max_i = i

print(max_cnt, max_i)
