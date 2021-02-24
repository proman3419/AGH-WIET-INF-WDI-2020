n = int(input())

a = b = 1
min_diff = n - 1
for i in range(2, int(n**0.5)+1):
  if n % i == 0:
    _a = i
    _b = n//i
    diff = abs(_a-_b)
    if diff < min_diff:
      min_diff = diff
      a = _a
      b = _b

print(a, b)
