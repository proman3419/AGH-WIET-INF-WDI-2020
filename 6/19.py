from random import randint, seed
from math import log10


def check_if_reachable(w, k, corner, prev_w=-1, prev_k=-1, path=''):
  if w < 0 or w >= N or k < 0 or k >= N: return
  if prev_w != -1 and T[prev_w][prev_k]%10 >= T[w][k]//10**(int(log10(T[w][k]))): return
  path += f'({w}, {k}) '
  if w == c[0]:
    if k == c[1]: 
      print(path)
      exit()
    return

  for cds in corner[2]:
    check_if_reachable(w+cds[0], k+cds[1], corner, w, k, path)


# seed(3)
N, w, k = map(int, input().split())
corners = ((0, 0, ((0, -1), (-1, 0), (-1, -1))), 
           (0, N-1, ((0, 1), (-1, 0), (-1, 1))), 
           (N-1, 0, ((0, -1), (1, 0), (1, -1))), 
           (N-1, N-1, ((0, 1), (1, 0), (1, 1))))
rr = (0, 99)
T = [[randint(rr[0], rr[1]) for _ in range(N)] for _ in range(N)]

for r in T:
  print(r)
for c in corners:
  check_if_reachable(w, k, c)

print(False)
