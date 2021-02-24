from random import randint


def check(data):
  for i in range(N):
    for j in range(i+1, N):
      if data[i][0] == data[j][0] or data[i][1] == data[j][1]: return False
      if (abs(data[i][0]-data[j][0]) == abs(data[i][1]-data[j][1])): return False
        
  return True


N = int(input())
data = [(randint(0, 9), randint(0, 9)) for _ in range(N)]
board = [[('*', '*') for _ in range(10)] for _ in range(10)]

for d in data:
  board[d[0]][d[1]] = (str(d[0]), str(d[1]))

for r in board:
  print(r)

print(check(data))
