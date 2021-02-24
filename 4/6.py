from random import randint


def copy_singleton_sort(T1, T2, N):
  ids = [0]*N
  _id = 0
  considered = 0
  while considered < N*N:
    _min = 10**100
    _min_id = -1 
    for i in range(N):
      if ids[i] < N and T1[i][ids[i]] < _min:
        _min_id = i
        _min = T1[i][ids[i]]

    cnt = 0
    for i in range(N):
      while ids[i] < N and T1[i][ids[i]] == _min:
        ids[i] += 1
        cnt += 1

    if cnt == 1:
      T2[_id] = _min
      _id += 1
    considered += 1

  return T2


N = int(input())
T1 = []
for i in range(N):
  T1.append(sorted([randint(-100, 100) for j in range(N)]))

for r in T1:
  print(r)
T2 = [0]*(N*N)

print(copy_singleton_sort(T1, T2, N))
