from random import randint


def longest_ari_seq(t, N):
  longest_inc = 0
  longest_dec = 0
  for i in range(N-1):
    curr = 1
    diff = t[i+1] - t[i]
    for j in range(i+1, N):
      if t[j] - t[j-1] == diff:
        curr += 1
      else:
        break
    if diff > 0 and curr > longest_inc:
      longest_inc = curr
    elif diff < 0 and curr > longest_dec:
      longest_dec = curr

  return (longest_inc, longest_dec)


N = int(input())
t = [randint(1, 99) for i in range(N)]
print(t)
longest_inc, longest_dec = longest_ari_seq(t, N)
print(longest_inc, longest_dec, longest_inc-longest_dec)
