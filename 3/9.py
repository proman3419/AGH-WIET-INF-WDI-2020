from random import randint


def longest_inc_seq(t, N):
  longest = 0
  for i in range(N):
    curr = 0
    for j in range(i+1, N):
      if t[j] <= t[i]:
        break
      curr += 1
    if curr > longest:
      longest = curr

  return longest


N = int(input())
t = [randint(0, 1000) for i in range(N)]
print(t)
print(longest_inc_seq(t, N))
