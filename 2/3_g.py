# a%10 - ostatnia cyfra
# a//10 - usuwa ostatnia cyfre
# a = 10*a + c - dopisuje c do konca liczby

n = int(input())
_n = n

rewers = 0
while _n > 0:
  rewers = rewers*10 + _n%10
  _n //= 10

print('10: yes') if n == rewers else print('10: no')

rewers = 0
_n = n
while _n > 0:
  rewers = rewers*2 + _n%2
  _n //= 2

print('2: yes') if n == rewers else print('2: no')
