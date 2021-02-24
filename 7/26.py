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


def is_sublist(head2, head1):
  curr1 = head1
  while curr1 is not None:
    _curr1 = curr1.next
    curr2 = head2.next
    while _curr1 is not None and curr2 is not None and _curr1.val == curr2.val:
      _curr1 = _curr1.next
      curr2 = curr2.next
    if curr2 is None:
      return True

    curr1 = curr1.next

  return False


head1 = Node()
add(head1, 1)
add(head1, 2)
add(head1, 3)
add(head1, 4)
add(head1, 5)
add(head1, 6)

head2 = Node()
add(head2, 3)
add(head2, 4)
add(head2, 5)

print(is_sublist(head2, head1))
