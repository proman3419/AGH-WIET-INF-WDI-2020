class Node:
  def __init__(self):
    self.val = None
    self.next = None


class AlmostEmptyList:
  def __init__(self, n):
    self.head = Node()
    curr = self.head
    for i in range(n):
      curr.next = Node()
      curr = curr.next
    self.tail = curr

  def get(self, n):
    curr = self.head
    for i in range(n+1):
      if curr.next is None:
        return None
      curr = curr.next

    return curr.val

  def insert(self, n, val):
    curr = self.head
    for i in range(n+1):
      if curr.next is None:
        return
      curr = curr.next

    curr.val = val

  def print(self):
    if self.head.next is not None:
      curr = self.head.next
      while True:
        print(curr.val, end=' ')
        if curr.next is not None:
          curr = curr.next
        else:
          print()
          break


ael = AlmostEmptyList(10)
ael.insert(0, 20)
ael.insert(1, 50)
ael.insert(2, 30)
ael.insert(9, 40)
ael.print()
print(ael.get(1))
print(ael.get(3))
print(ael.get(4))
