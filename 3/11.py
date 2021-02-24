from random import randint


def longest_inc_geo_seq(t, N):
  longest = 0
  for i in range(N-1):
    curr = 1
    div = t[i+1]/t[i]
    for j in range(i+1, N):
      if t[j]/t[j-1] == div:
        curr += 1
      else:
        break
    if curr > longest:
      longest = curr

  return longest


N = int(input())
t = [randint(1, 10) for i in range(N)]
print(t)
print(longest_inc_geo_seq(t, N))
