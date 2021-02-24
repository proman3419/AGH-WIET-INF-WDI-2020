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


def ll_length(head):
  _len = 0
  curr = head.next
  while curr is not None:
    curr = curr.next
    _len += 1

  return _len


def add_zeros(head, n):
  for i in range(n):
    temp = head.next
    head.next = Node(0)
    head.next.next = temp


def sum(head1, head2):
  def sum_rec(curr1, curr2, curr3):
    curr3.next = Node()
    curr3 = curr3.next

    # no need to check curr2, _len1 == _len2
    if curr1.next is None:
      curr3.val = curr1.val + curr2.val
      rest = curr3.val//10
      curr3.val %= 10
      return rest

    rest = sum_rec(curr1.next, curr2.next, curr3)

    if curr3.val is None:
      curr3.val = curr1.val + curr2.val
    curr3.val += rest
    rest = curr3.val//10
    curr3.val %= 10

    return rest

  _len1 = ll_length(head1)
  _len2 = ll_length(head2)
  if _len1 > _len2:
    add_zeros(head2, _len1-_len2)
  else:
    add_zeros(head1, _len2-_len1)    

  head3 = Node()
  rest = sum_rec(head1.next, head2.next, head3)
  if rest != 0:
    temp = head3.next
    head3.next = Node(rest)
    head3.next.next = temp 

  return head3


head1 = Node()
add(head1, 9)
add(head1, 9)
add(head1, 9)
add(head1, 9)
head2 = Node()
add(head2, 1)
add(head2, 1)

display(sum(head1, head2))
