e = 0.5
a = 1
b = 10
A = 2020

while abs(a-b) > e:
  a, b = b, 1/b*((b-1)*b + A/(b**(b-1)))

print(b)
