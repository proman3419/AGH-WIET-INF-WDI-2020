from random import randint


def resistance(r_positions):
  res = sum(r_positions[0])
  _sum = sum(r_positions[1])
  if _sum != 0:
    res += 1/_sum

  return res


def check_if_res_possible(T, N, R, chosen, chid=0, i=0):
  if chid == 3:
    r_positions = [[0]*3, [0]*3]
    for j in range(2**3):
      for k in range(3):
        r_positions[j%2][k] = T[chosen[k]]
        j //= 2

      if resistance(r_positions) == R:
        flag[0] = True
        return

      for k in range(3):
        r_positions[0][k] = r_positions[1][k] = 0

    return

  for j in range(i+1, N):
    if flag[0]: return
    _chosen = chosen[:]
    _chosen[chid] = j
    check_if_res_possible(T, N, R, _chosen, chid+1, j)


N = int(input())
R = float(input())
rr = (1, 2)
T = [randint(rr[0], rr[1]) for _ in range(N)]
flag = [False]

print(T)
check_if_res_possible(T, N, R, [-1, -1, -1])
print(*flag)
