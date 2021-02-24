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


def sort_and_reduce(head1, head2):
  curr2 = head2.next
  while curr2 is not None:
    prev1 = head1
    curr1 = head1.next
    while curr1 is not None and curr1.val < curr2.val:
      prev1, curr1 = curr1, curr1.next

    _next = curr2.next

    if curr1 is None or curr2.val != curr1.val:
      prev1.next = curr2
      curr2.next = curr1

    curr2 = _next


head1 = Node()  
add(head1, 2)
add(head1, 3)

head2 = Node()  
add(head2, 8)
add(head2, 2)
add(head2, 7)
add(head2, 4)

sort_and_reduce(head1, head2)
display(head1)
