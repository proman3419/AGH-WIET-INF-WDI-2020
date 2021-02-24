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


def remove_longest_inc_seq(head):
  if head.next is None:
    return
  
  prev = head
  curr = head.next
  curr_seq = [head, head, 0]
  _max_seq = [None, None, 1]
  flag = False
  while curr.next is not None:
    curr_seq[0] = prev
    curr_seq[2] = 1
    while curr.next is not None and curr.val < curr.next.val:
      curr_seq[1] = curr
      curr_seq[2] += 1   
      curr = curr.next

    if curr_seq[2] > _max_seq[2]:
      flag = True
      _max_seq[0] = curr_seq[0]
      _max_seq[1] = curr_seq[1].next
      _max_seq[2] = curr_seq[2]
    elif curr_seq[2] == _max_seq[2]:
      flag = False

    prev, curr = curr, curr.next
    if curr is None:
      break

  if flag:
    _max_seq[0].next = _max_seq[1].next


head = Node()
add(head, 1)
add(head, 2)
add(head, 3)
add(head, 1)
add(head, 4)
add(head, 5)
remove_longest_inc_seq(head)
display(head)
