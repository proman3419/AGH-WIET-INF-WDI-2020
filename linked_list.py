class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None


def add(head, val):
  curr = head
  while curr.next is not None:
    curr = curr.next

  curr.next = Node(val)


def sort_add(head, val):
  if head.next is None:
    head.next = Node(val)
  else:
    prev = head
    curr = head.next
    while curr is not None and curr.val < val:
      prev, curr = curr, curr.next

    prev.next = Node(val)
    prev.next.next = curr


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


head = Node()

