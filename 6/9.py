from random import randint


def func(i, w, path):
  if abs(w) == target_w: return path
  if i == N: return False

  return func(i+1, w+T[i], f'{path}A:{T[i]} ') or func(i+1, w-T[i], f'{path}B:{T[i]} ') or func(i+1, w, path)


N, target_w = map(int, input().split())
rr = (1, 10)
T = [randint(rr[0], rr[1]) for _ in range(N)]
print(T)
print(func(0, 0, ''))
