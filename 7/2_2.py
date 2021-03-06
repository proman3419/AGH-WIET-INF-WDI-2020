class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None


def add(head, val):
  curr = head
  while curr.next is not None:
    curr = curr.next

  curr.next = Node(val)


def insert(head, val):
  if head.next is None:
    add(head, val)
  else:
    temp = head.next
    head.next = Node(val)
    head.next.next = temp


def remove(head, val, _all=True):
  curr = head
  while curr.next is not None:
    if curr.next.val == val:
      curr.next = curr.next.next
      if not _all:
        return
    else:
      curr = curr.next


def contains(head, val):
  curr = head
  while curr is not None:
    if curr.val == val:
      return True
    curr = curr.next

  return False


def ll_length(head):
  _len = 0
  curr = head.next
  while curr is not None:
    curr = curr.next
    _len += 1

  return _len


def display(head):
  print(head.val, end=' ')
  curr = head.next
  while curr is not None:
    print('->', curr.val, end=' ')
    curr = curr.next
  print()


##########################################################################


def init(head, _len):
  curr = head
  for i in range(_len):
    curr.next = Node()
    curr = curr.next


def get_by_id(head, _id):
  curr = head.next
  while curr is not None and _id > 0:
    curr = curr.next
    _id -= 1

  if _id == 0:
    return curr.val

  return None


def change_at_id(head, _id, val):
  curr = head.next
  while curr is not None and _id > 0:
    curr = curr.next
    _id -= 1

  if _id == 0:
    curr.val = val


head = Node()
init(head, 3)
change_at_id(head, 0, 30)
change_at_id(head, 1, 40)
change_at_id(head, 2, 50)
change_at_id(head, 1, 660)
display(head)
print(get_by_id(head, -1))
