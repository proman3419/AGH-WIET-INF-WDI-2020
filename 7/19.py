class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None


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
    while curr is not None and curr.val < val:
      prev, curr = curr, curr.next

    prev.next = Node(val)
    prev.next.next = curr


def remove_duplicates(head):
  cnt = 0
  prev = head
  curr = head.next
  while curr is not None:
    flag = False
    _prev = curr
    _curr = curr.next
    while _curr is not None and _curr.val < curr.val:
      _prev, _curr = _curr, _curr.next

    while _curr is not None and _curr.val == curr.val:
      _curr = _curr.next
      cnt += 1
      flag = True

    _prev.next = _curr

    if flag:
      prev.next = curr.next
      cnt += 1

    prev, curr = curr, curr.next

  return cnt


head = Node()  
sort_add(head, 1)
sort_add(head, 3)
sort_add(head, 3)
sort_add(head, 3)
sort_add(head, 3)
sort_add(head, 10)
sort_add(head, 5)
display(head)
print(remove_duplicates(head))
display(head)
