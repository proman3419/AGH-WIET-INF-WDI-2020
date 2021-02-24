a1 = 0
a2 = 1
b = 2

while a2 == int(input()):
  b = b + 2*a1
  print(b)
  a1, a2 = a2, a2 - b*a1
