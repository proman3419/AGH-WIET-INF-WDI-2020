from random import randint


def func(i, w):
  if w == target_w: return True
  if i == N: return False

  return func(i+1, w+T[i]) or func(i+1, w)


N, target_w = map(int, input().split())
rr = (1, 10)
T = [randint(rr[0], rr[1]) for _ in range(N)]
print(T)
print(func(0, 0))
