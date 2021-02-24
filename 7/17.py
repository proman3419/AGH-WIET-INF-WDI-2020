class Node:
  def __init__(self, val=None):
    self.val = val
    self.prev = None
    self.next = None


def add(head, val):
  prev = None
  curr = head
  while curr.next is not None:
    prev, curr = curr, curr.next

  curr.next = Node(val)
  curr.next.prev = curr


def display(head):
  print(head.val, end=' ')
  curr = head.next
  while curr is not None:
    print('->', curr.val, end=' ')
    curr = curr.next
  print()


def display_reverse(head):
  curr = head
  while curr.next is not None:
    curr = curr.next

  while curr.prev is not None:
    print(curr.val, '->' , end=' ')
    curr = curr.prev
  print(None)


def odd_ones_in_bin(n):
  cnt = 0
  while n > 0:
    cnt += n % 2
    n //= 2

  return cnt % 2 == 1


def remove_with_cond(head):
  prev = head
  curr = head.next
  while curr is not None:
    if odd_ones_in_bin(curr.val):
      prev.next = curr.next
      if curr.next is not None:
        curr.next.prev = prev
      curr = curr.next
    else:
      prev, curr = curr, curr.next


head = Node()  
add(head, 10) #o
add(head, 1) #x
add(head, 2) #x
add(head, 3) #o
add(head, 4) #x
add(head, 8) #x
add(head, 5) #o
add(head, 7) #o
remove_with_cond(head)
display(head)
display_reverse(head)
