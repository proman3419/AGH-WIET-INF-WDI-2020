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


def split(head):
  heads = [Node(), Node()]
  currs = [heads[0], heads[1]]
  prev = head
  curr = head.next
  cnt = 0
  while curr is not None:
    _next = curr.next
    curr.next = None
    if curr.val > 0 and curr.val % 2 == 0:
      currs[0].next = curr
      currs[0] = currs[0].next
    elif curr.val < 0 and abs(curr.val) % 2 == 1:
      currs[1].next = curr
      currs[1] = currs[1].next
    else:
      prev.next = curr.next
      cnt += 1

    curr = _next

  return (heads, cnt)


head = Node()  
add(head, 1)
add(head, 2)
add(head, 4)
add(head, 5)
add(head, -3)
add(head, -7)
add(head, 0)

heads, cnt = split(head)
print(cnt)
display(heads[0])
display(heads[1])
