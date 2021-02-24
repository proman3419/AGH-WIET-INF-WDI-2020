def queens():
  T = [-1]*8
  Tw = [True]*8
  T1 = [True]*15
  T2 = [True]*15

  def place_queen(w, k):
    if not (Tw[w] and T1[w+k] and T2[w-k+7]): return
    
    T[k] = w
    if k != 7:
      Tw[w] = T1[w+k] = T2[w-k+7] = False
      for i in range(8):
        place_queen(i, k+1)
      Tw[w] = T1[w+k] = T2[w-k+7] = True
    else:
      print(T)
    
  for i in range(8):
    place_queen(i, 0)


queens()
