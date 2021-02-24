import math


n = int(input())
_sum = 0
i = 1

while _sum <= n:
  _sum += i
  i += 2
  
print(int(math.sqrt(_sum)-1))
