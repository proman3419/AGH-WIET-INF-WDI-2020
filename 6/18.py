from random import randint, seed
from math import log10


def check_if_reachable(w, k, prev_w=-1, prev_k=-1, path=''):
  if w < 0 or w >= N or k >= N: return False
  if prev_w != -1 and T[prev_w][prev_k]%10 >= T[w][k]//10**(int(log10(T[w][k]))): return False
  path += f'({w}, {k}) '
  if w == N-1:
    if k == N-1: 
      print(path)
      return True
    return False

  return check_if_reachable(w, k+1, w, k, path) or \
         check_if_reachable(w+1, k, w, k, path) or \
         check_if_reachable(w+1, k+1, w, k, path)
         

seed(3)
N, w, k = map(int, input().split())
rr = (0, 99)
T = [[randint(rr[0], rr[1]) for _ in range(N)] for _ in range(N)]

for r in T:
  print(r)
print(check_if_reachable(w, k))
