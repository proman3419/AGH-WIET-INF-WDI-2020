from random import randint


#N = int(input())
#t = [randint(100, 999) for i in range(N)]
N = len(t)
t = [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
print(t)

_max = 0
for i in range(N):
  for j in range(N-1, -1, -1):
    cnt = 0
    _i = i
    _j = j
    
    while _i < N and _j >= 0 and t[_i] == t[_j]:
      _i += 1
      _j -= 1
      cnt += 1

    if cnt > _max:
      _max = cnt

print(_max)
