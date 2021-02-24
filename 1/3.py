target_sum = int(input())
_max = 10**6
a = b = 1
_sum = a + b
fib = [a, b]

while _sum < target_sum:
  a, b = b, a+b
  _sum += b
  fib.append(b)

i = 0
while _sum > target_sum:
  _sum -= fib[i]
  i += 1

if _sum == target_sum:
  print('exists')
else:
  print('doesnt exist')
