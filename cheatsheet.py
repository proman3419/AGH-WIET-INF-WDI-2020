# constants
vectors = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
vowels = 'aeiouy'


# is_prime
def is_prime(n):
  if n < 2: return False
  if n == 2: return True
  if n % 2 == 0: return False

  i = 3
  while i*i <= n:
    if n % i == 0:
      return False
    i += 2
    
  return True


# number_len
from math import log10
def number_len(n):
  return int(log10(n)) + 1


# points distance
def distance(p1, p2):
  return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)


# gcd
def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)

# lcm
def lcm(a, b):
  return a//gcd(a, b)*b//gcd(a, b)


# sum_digits
def sum_digits(n):
  _sum = 0
  while n > 0:
    _sum += n%10
    n //= 10
  return _sum


# cnt_prime_factors
def cnt_prime_factors(n):
  cnt = 0
  i = 2
  while n > 1:
    if n % i == 0:
      cnt += 1
      while n % i == 0:
        n //= i
    i += 1
  return cnt


# factorize
def factorize(n):
  factors = []
  i = 2
  while n > 1:
    if n % i == 0:
      factors.append(i)
      while n % i == 0:
        n //= i
    i += 1
  return factors


# revert_list
def revert_list(T):
  N = len(T)
  i = 0
  while i < N//2:
    T[i], T[N-1-i] = T[N-1-i], T[i]
    i += 1
        
  return T


# revert num
def revert_num(n):
  _n = 0
  while n > 0:
    _n = _n*10 + n%10
    n //= 10
  return _n

# is_palindrome
def is_palindrome(n):
  return n == revert_num(n)


# bubble_sort
def bubble_sort(T):
  N = len(T)
  for i in range(N):
    for j in range(N):
      if T[i] < T[j]:
        T[i], T[j] = T[j], T[i]


# rooks check
def check_sums(t, N):
  row_sums = [0]*N
  col_sums = [0]*N
  for row in range(N):
    for col in range(N):
      row_sums[row] += t[row][col]

  for col in range(N):
    for row in range(N):
      col_sums[col] += t[row][col]

  return (row_sums, col_sums)

def rooks_check(t, row_sums, col_sums, r1, c1, r2, c2):
  res = row_sums[r1] + col_sums[c1] - 2*t[r1][c1] - 2*t[r2][c2]
  if r1 == r2:
    res += col_sums[c2]
  elif c1 == c2:
    res += row_sums[r2]
  else:
    res += row_sums[r2] + col_sums[c2] - t[r1][c2] - t[r2][c1]

  return res

N = int(input())
rr = (1, 4)
t = [[randint(rr[0], rr[1]) for _ in range(N)] for _ in range(N)]

for r in t:
  print(r)
row_sums, col_sums = check_sums(t, N)
print(rooks_check(t, row_sums, col_sums, 0, 0, 1, 2))


# randint array 1D
from random import randint
N = int(input())
rr = (1, 10)
T = [randint(rr[0], rr[1]) for _ in range(N)]


# randint array 2D
from random import randint
N = int(input())
rr = (1, 10)
T = [[randint(rr[0], rr[1]) for _ in range(N)] for _ in range(N)]
