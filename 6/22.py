from random import randint


def jump_rec(T, N, i=0, jumps=0):
  if i == N-1: res[0] = jumps
  if i > N-1: return

  for j in range(N):
    if res[0] != -1: return
    n = T[i]
    k = 2
    while n > 1:
      if n % k == 0 and n != k:
        jump_rec(T, N, i+k, jumps+1)
      while n % k == 0:
        n //= k
      k += 1


N = int(input())
rr = (49, 49)
T = [randint(rr[0], rr[1]) for _ in range(N)]
res = [-1]

print(T)
jump_rec(T, N)
print(res[0])
