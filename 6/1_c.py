def func(n, N, k=0, l=0):
  if n == 0:
    if k != N and k >= 10:
      res.add(k)
      print(k)
    return

  func(n//10, N, k+(n%10)*(10**l), l+1)
  func(n//10, N, k, l)


res = set()
N = 1233
func(N, N)

print(res)