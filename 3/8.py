def sieve(n):
  n += 1
  a = [True]*n

  i = 2
  while i*i < n:
    if a[i]:
      for j in range(i*i, n, i):
        a[j] = False
    i += 1

  return [i for i in range(2, n) if a[i]]


t = [7, 2, 3, 4, 5, 6, 9, 11]
N = len(t)

_max = t[0]
for e in t[1:]:
  if e > _max:
    _max = e

primes = sieve(_max)
_len_primes = len(primes)
k_possible_moves = {}

for e in t:
  k_possible_moves[e] = [False]*_len_primes

for e in t:
  for i in range(_len_primes):
    if e % primes[i] == 0:
      k_possible_moves[e][i] = True

for pm in k_possible_moves[t[0]]:
  left = N - 1
  if pm:
    left -= pm
    while 
