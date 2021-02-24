from random import randint


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


def divide(head, heads):
  curr = head.next
  while curr is not None:
    _id = curr.val % 10
    add(heads[_id], curr.val)
    curr = curr.next


def combine(heads):
  head = heads[0]
  for i in range(9):
    curr = heads[i]
    while curr.next is not None:
      curr = curr.next
    curr.next = heads[i+1]

  # remove useless wardens
  remove(head, None)

  return head


head = Node()
N = int(input())
rr = (1, 100)
for i in range(N):
  add(head, randint(rr[0], rr[1]))
display(head)

heads = [Node() for _ in range(10)]
divide(head, heads)

head = combine(heads)
display(head)
