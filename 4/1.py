def generuj_spirale(tab):
  n = len(tab)
  k = 1
  a = 0
  b = n-1
  while a <= b:
    for i in range(a, b+1):
      tab[a][i] = k
      k += 1

    for i in range(a+1, b):
      tab[i][b] = k
      k += 1

    for i in range(b, a, -1):
      tab[b][i] = k
      k += 1

    for i in range(b, a, -1):
      tab[i][a] = k
      k += 1
    a += 1
    b -= 1
    
  for line in tab:
    for elem in line:
      print(str(elem).rjust(5), end="")
    print("")


N = int(input())
generuj_spirale([[0 for _ in range(N)] for _ in range(N)])
