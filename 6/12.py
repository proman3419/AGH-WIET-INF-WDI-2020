from random import randint


def func(i, m, s):
  if i == N:
    if m == target_m:
      return s + '\n'
    return ''

  return func(i+1, m*T[i], f'{s}{T[i]} ') + func(i+1, m, s)


N, target_m = map(int, input().split())
rr = (1, 5)
T = [randint(rr[0], rr[1]) for _ in range(N)]
print(T)
print(func(0, 1, ''))