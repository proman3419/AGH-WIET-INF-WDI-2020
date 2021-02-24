def field(sq):
  return abs(sq[0]-sq[1])*abs(sq[2]-sq[3])


def contains(sq1, sq2):
  if sq1[0] > sq2[1] or sq1[1] < sq2[0] or \
     sq1[2] > sq2[3] or sq1[3] < sq2[2]:
    return False

  return True


def check_sqs(T, N, taken, i=0, j=0, _len=0, field_sum=0):
  if j > 1:
    k = 0
    while k < 3 and taken[k] != -1:
      if k != j-1:
        if contains(T[taken[k]], T[taken[j-1]]):
          return False
      k += 1

  # 13
  if _len == 3:
    # 2012
    if field_sum == 9:
      return True
    return False

  if i == N:
    return False

  _taken1 = taken[:]
  _taken2 = taken[:]
  _taken2[j] = i
  return check_sqs(T, N, _taken1, i+1, j, _len, field_sum) or \
         check_sqs(T, N, _taken2, i+1, j+1, _len+1, field_sum+field(T[i]))


T = [[0, 1, 0, 1]
     ]
N = len(T)

taken = [-1]*3
print(check_sqs(T, N, taken))
