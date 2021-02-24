from random import randint


def create(args=None):
  if args is None:
    l, m = map(int, input().split())
    return (l, m)
  return (randint(args[0], args[1]), randint(args[0], args[1]))


def output(n):
  print(f'{n[0]}/{n[1]}')


def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)


def lcm(a, b):
  return a*b//gcd(a, b)


def add(a, b):
  _lcm = lcm(a[1], b[1])
  return (a[0]*_lcm//a[1] + b[0]*_lcm//b[1], _lcm)


def sub(a, b):
  _lcm = lcm(a[1], b[1])
  return (a[0]*_lcm//a[1] - b[0]*_lcm//b[1], _lcm)


def multiply(a, b):
  return (a[0]*b[0], a[1]*b[1])


def div(a, b):
  return (a[0]*b[1], a[1]*b[0])


def simplify(a):
  _gcd = gcd(a[0], a[1])
  return (a[0]//_gcd, a[1]//_gcd)


def equal(a, b):
  return a[0] == b[0] and a[1] == b[1]


def check_ari(nums, N):
  i = 0
  cnt = 0
  while i < N - 1:
    r = simplify(sub(nums[i+1], nums[i]))
    _len = 2
    for j in range(i+1, N-1):
      if not equal(simplify(sub(nums[j+1], nums[j])), r):
        break
      _len += 1

    if _len > 2:
      for j in range(2, _len):
        cnt += _len - j
      i += _len
    else:
      i += 1

  return cnt


def check_geo(nums, N):
  i = 0
  cnt = 0
  while i < N - 1:
    if nums[i][1] != 0:
      r = simplify(div(nums[i+1], nums[i]))
      _len = 2
      for j in range(i+1, N-1):
        if not equal(simplify(div(nums[j+1], nums[j])), r):
          break
        _len += 1

      if _len > 2:
        for j in range(2, _len):
          cnt += _len - j
        i += _len
      else:
        i += 1

  return cnt


def compare_ari_geo(nums, N):
  LA = check_ari(nums, N)
  LG = check_geo(nums, N)
  if LA < LG: return -1
  if LA > LG: return 1
  if LA == LG: return 0


randint_range = (1, 3)
N = int(input())
nums = [create(randint_range) for _ in range(N)]

for n in nums:
  output(n)

print(compare_ari_geo(nums, N))
