from random import randint


tests = 1000
cnt = 0
people = [0]*40
for N in range(20, 41):
  i = 0
  for t in range(tests):
    while i < N:
      people[i] = randint(1, 365)

      for j in range(i-1, -1, -1):
        if people[i] == people[j]:
          cnt += 1
          i = N
          break

      i += 1

  print(f'{N}: {cnt/tests*100}%')
