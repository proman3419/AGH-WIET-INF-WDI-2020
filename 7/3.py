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


def merge_iter(head1, head2):
  head3 = Node()
  curr1 = head1.next
  curr2 = head2.next
  curr3 = head3

  while curr1 is not None and curr2 is not None:
    if curr1.val <= curr2.val:
      curr3.next = curr1
      curr1 = curr1.next
    else:
      curr3.next = curr2
      curr2 = curr2.next
    curr3 = curr3.next

  while curr1 is not None:
    curr3.next = curr1
    curr3 = curr3.next
    curr1 = curr1.next

  while curr2 is not None:
    curr3.next = curr2
    curr3 = curr3.next
    curr2 = curr2.next

  return head3


def merge_rec(head1, head2):
  def _merge_rec(curr1, curr2, curr3):
    if curr1 is None and curr2 is None:
      return

    if curr1 is not None and curr2 is not None:
      if curr1.val <= curr2.val:
        curr3.next = curr1
        curr1 = curr1.next
      else:
        curr3.next = curr2
        curr2 = curr2.next
      curr3 = curr3.next
      _merge_rec(curr1, curr2, curr3)

    elif curr1 is not None:
      curr3.next = curr1
      curr3 = curr3.next
      curr1 = curr1.next
      _merge_rec(curr1, curr2, curr3)

    else:
      curr3.next = curr2
      curr3 = curr3.next
      curr2 = curr2.next
      _merge_rec(curr1, curr2, curr3)

  head3 = Node()
  curr1 = head1.next
  curr2 = head2.next
  curr3 = head3
  _merge_rec(curr1, curr2, head3)

  return head3


head1 = Node()
head2 = Node()
add(head1, 1)
add(head1, 5)
add(head1, 6)
add(head2, 2)
add(head2, 4)
add(head2, 8)
add(head2, 11)
add(head2, 999)
#head3 = merge_iter(head1, head2)
head3 = merge_rec(head1, head2)
display(head3)
