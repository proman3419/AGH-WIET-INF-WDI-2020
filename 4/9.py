from random import randint


def find_square(T, N, k):
  for i in range(N-2):
    for j in range(N-2):
      a = 2
      flag = True
      while flag:
        c_ids = [i+a, j+a]
        for c_id in c_ids:
          if c_id >= N:
            flag = False
            break
        else:
          if T[i][j]*T[c_ids[0]][j]*T[i][c_ids[1]]*T[c_ids[0]][c_ids[1]] == k:
            center = a//2
            return (True, i+center, j+center)
          a += 2

  return False


N, k = map(int, input().split())
T = []
for i in range(N):
  T.append(sorted([randint(1, 3) for j in range(N)]))

for r in T:
  print(r)
print(find_square(T, N, k))
