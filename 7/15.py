class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None


def add(head, val):
  curr = head
  while curr.next is not None:
    curr = curr.next

  curr.next = Node(val)


def insert(head, val):
  if head.next is None:
    add(head, val)
  else:
    temp = head.next
    head.next = Node(val)
    head.next.next = temp


def remove(head, val):
  curr = head
  while curr.next is not None:
    if curr.next.val == val:
      curr.next = curr.next.next
      return
    else:
      curr = curr.next


def remove_all(head, val):
  curr = head
  while curr.next is not None:
    if curr.next.val == val:
      curr.next = curr.next.next
    else:
      curr = curr.next


def contains(head, val):
  curr = head
  while curr is not None:
    if curr.val == val:
      return True
    curr = curr.next

  return False


def ll_length(head):
  _len = 0
  curr = head.next
  while curr is not None:
    curr = curr.next
    _len += 1

  return _len


def display(head):
  print(head.val, end=' ')
  curr = head.next
  while curr is not None:
    print('->', curr.val, end=' ')
    curr = curr.next
  print()


##########################################################################


def more_ones_than_twos(n):
  cnts = [0, 0, 0]
  while n > 0:
    cnts[n%3] += 1
    n //= 3

  return cnts[1] > cnts[2]


def rem_base3(head):
  prev = head
  curr = head.next

  while curr is not None:
    if more_ones_than_twos(curr.val):
      prev.next = curr.next
      curr = curr.next
    else:
      prev, curr = curr, curr.next


head = Node()
insert(head, 1)
insert(head, 2)
insert(head, 5)
insert(head, 7)
insert(head, 8)
insert(head, 9)
insert(head, 10)
insert(head, 11)
insert(head, 12)
insert(head, 13)
insert(head, 33)
insert(head, 3)
rem_base3(head)
display(head)
