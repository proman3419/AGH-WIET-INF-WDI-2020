from random import randint


def longest_geo_seq_diag(T, N):
  _max_len = 0
  for i in range(N-2):
    for j in range(N-2):
      _i = i
      k = i + 1
      l = j + 1
      q = T[k][l]/T[i][j]
      _len = 1
      while k < N and l < N and q == T[k][l]/T[_i][j]:
        _i += 1
        j += 1
        k += 1
        l += 1
        _len += 1

      if _len > _max_len:
        _max_len = _len

  if _max_len >= 3:
    return (True, _max_len)
  return False


N = int(input())
T = []
for i in range(N):
  T.append(sorted([randint(1, 10) for j in range(N)]))

for r in T:
  print(r)
print(longest_geo_seq_diag(T, N))
