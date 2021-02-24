def print_board():
  for r in T:
    print(r)


def func(x, y, cnt):
  T[x][y] = cnt
  if cnt == target_cnt:
    return True
  else:
    for v in vectors:
      _x = x + v[0]
      _y = y + v[1]
      if 0 <= _x and _x < N and 0 <= _y and _y < N:
        if T[_x][_y] == 0:
          if func(_x, _y, cnt+1):
            return True

    T[x][y] = 0
    return False


N = int(input())
T = [[0 for _ in range(N)] for _ in range(N)]
target_cnt = N*N
vectors = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))

for x in range(N):
  for y in range(N):
    if func(x, y, 1):
      print_board()
      exit()

print('no solution')
