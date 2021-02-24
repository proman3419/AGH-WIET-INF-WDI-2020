from random import randint


def calculate_ceons(T, N, i=0, x=0, y=0, taken=0):
  if i == N:
    if taken != 0:
      ceons.append((x/taken, y/taken))
    return

  print(i)
  calculate_ceons(T, N, i+1, x, y, taken)
  calculate_ceons(T, N, i+1, x+T[i][0], y+T[i][1], taken+1)


def min_distance(ceons, N):
  _min_dist = 10**100
  for i in range(N):
    for j in range(N):
      if i != j:
        dist = ((ceons[i][0]-ceons[j][0])**2 + (ceons[i][1]-ceons[j][1])**2)
        if dist < _min_dist:
          _min_dist = dist

  return _min_dist


N = int(input())
rr = (1, 10)
T = [tuple((randint(rr[0], rr[1]), randint(rr[0], rr[1]))) for _ in range(N)]
ceons = []

calculate_ceons(T, N)
print(ceons)
print(min_distance(ceons, len(ceons)))
