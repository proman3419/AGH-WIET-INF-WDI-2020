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

def reverse(head):
  prev = None
  # next because of the warden
  curr = head.next

  while curr is not None:  
    _next = curr.next
    curr.next = prev
    prev, curr = curr, _next

  # add a warden
  temp = prev
  prev = Node()
  prev.next = temp

  return prev


head = Node()
add(head, 1)
add(head, 2)
add(head, 3)
add(head, 4)
add(head, 5)
display(head)
head2 = reverse(head)
display(head2)
