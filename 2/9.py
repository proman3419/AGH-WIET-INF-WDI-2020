def f(x):
  return 1/x


k = int(input()) 
field = 0
precision = 10**1
d = (k-1)/precision
x = 1

while x < k:
  field += f(x)*d
  x += d

print(field)
