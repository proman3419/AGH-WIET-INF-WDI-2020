def find_targets(s):
  target_vowels_cnt = 0
  target_ord_sum = 0
  for ch in s:
    if ch in vowels:
      target_vowels_cnt += 1
    target_ord_sum += ord(ch)

  return (target_vowels_cnt, target_ord_sum)


def wyraz(s1, s2):
  targets = find_targets(s1)

  def recursive_check(s1, s2, targets, i=0, s='', vowels_cnt=0, ord_sum=0):
    if vowels_cnt == targets[0] and ord_sum == targets[1]:
      return s
    if i >= len(s1):
      return ''

    r1 = recursive_check(s1, s2, targets, i+1, s, vowels_cnt, ord_sum)
    if s1[i] in vowels: vowels_cnt += 1
    r2 = recursive_check(s1, s2, targets, i+1, s+s1[i], vowels_cnt, ord_sum+ord(s1[i]))

    return r1 if len(r1) > len(r2) else r2
    

  return recursive_check(s1, s2, targets)


vowels = 'aeiouy'
s1 = 'ula'
s2 = 'exe'
print(wyraz(s1, s2))
