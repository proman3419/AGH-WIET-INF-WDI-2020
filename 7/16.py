class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None


def add(head, val):
  curr = head
  while curr.next is not None:
    curr = curr.next

  curr.next = Node(val)


def display(head):
  print(head.val, end=' ')
  curr = head.next
  while curr is not None:
    print('->', curr.val, end=' ')
    curr = curr.next
  print()


##########################################################################


def even_fives_in_oct(n):
  cnt = 0
  while n > 0:
    if n % 8 == 5:
      cnt += 1
    n //= 8

  return cnt % 2 == 0


def move_to_front(head, prev, curr):
  prev.next = curr.next
  curr.next = head.next
  head.next = curr
  
  return prev.next


def reorganize(head):
  prev = head
  curr = head.next

  while curr is not None:
    if even_fives_in_oct(curr.val):
      curr = move_to_front(head, prev, curr)
    else:
      prev, curr = curr, curr.next


head = Node()  
add(head, 5)
add(head, 25)
add(head, 13)
add(head, 45)
add(head, 45)
reorganize(head)
display(head)
