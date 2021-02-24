from random import randint


def gen_dict(data, N):
  d = {}
  for e in data:
    d[e] = True

  return d


def collision(data, candidates):
  _min_x = min(candidates[0][0], candidates[1][0])
  _max_x = max(candidates[0][0], candidates[1][0])
  _min_y = min(candidates[0][1], candidates[1][1])
  _max_y = max(candidates[0][1], candidates[1][1])

  for p in data:
    if _min_x < p[0] and p[0] < _max_x and _min_y < p[1] and p[1] < _max_y:
      return True

  return False


def func(data, N):
  d = gen_dict(data, N)
  for i in range(N-1):
    for j in range(i+1, N):
      if data[i][0] - data[j][0] != 0 and data[i][1] - data[j][1] != 0:
        candidates = [(data[i][0], data[j][1]), (data[j][0], data[i][1])]
        if candidates[0] in d and candidates[1] in d:
          if not collision(data, candidates):
            return True

  return False


N = int(input())
randint_range = (0, 10)
data = [(randint(randint_range[0], randint_range[1]), randint(randint_range[0], randint_range[1])) for _ in range(N)]

for d in data:
  print(d)
print(func(data, N))
