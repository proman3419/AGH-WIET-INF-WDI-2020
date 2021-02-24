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


def sort_add(head, val):
  if head.next is None:
    head.next = Node(val)
  else:
    prev = head
    curr = head.next
    while curr is not None and curr.val[0] < val[0]:
      prev, curr = curr, curr.next

    prev.next = Node(val)
    prev.next.next = curr


def merge_ranges(head):
  prev = head
  curr = head.next
  while curr is not None:
    _prev = curr
    _curr = curr.next
    while _curr is not None:
      if _prev.val[1] >= _curr.val[0]:
        _prev.val[1] = _curr.val[1]
        _prev.next = _curr.next
      _prev, _curr = _curr, _curr.next

    prev, curr = curr, curr.next


head = Node()  
sort_add(head, [15, 19])
sort_add(head, [2, 5])1
sort_add(head, [7, 11])
sort_add(head, [8, 12])
sort_add(head, [5, 6])
sort_add(head, [13, 17])
sort_add(head, [17, 18])
sort_add(head, [18, 120])
display(head)
merge_ranges(head)
display(head)
