class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None


def add(head, val):
  curr = head
  while curr.next is not None:
    curr = curr.next

  curr.next = Node(val)


def remove(head, val):
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


def display(head):
  print(head.val, end=' ')
  curr = head.next
  while curr is not None:
    print('->', curr.val, end=' ')
    curr = curr.next
  print()


def increment(head):
  if head.next is None:
    return

  def increment_rec(curr):
    if curr.next is None:
      curr.val += 1
      rest = curr.val//10
      curr.val %= 10
      return rest

    rest = increment_rec(curr.next)
    curr.val += rest
    rest = curr.val//10
    curr.val %= 10
    return rest

  increment_rec(head.next)
  if head.next.val == 0:
    temp = head.next
    head.next = Node(1)
    head.next.next = temp


head = Node()
add(head, 1)
add(head, 1)
add(head, 9)
increment(head)
display(head)
