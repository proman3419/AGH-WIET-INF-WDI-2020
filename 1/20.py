import math


A, B = map(int, input().split())
e = 0.1**6

while abs(A-B) > e:
  A, B = math.sqrt(A*B), (A+B)/2

print(A)
