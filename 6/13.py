def func(n, p, prev):
  if n == 0:
    print(p)

  for i in range(prev, n+1):
    func(n-i, p+f'{i} ', i)


n = int(input())
func(n, '', 1)
