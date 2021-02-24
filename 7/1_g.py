class Node:

    def __init__(self, value = None):
        self.value = value
        self.next = None

def member(zbior, szukany):

    while zbior != None and zbior.value < szukany:
        zbior = zbior.next
    return zbior != None and zbior.value == szukany

def insert(start, n):
    p = start
    prev = None

    while p != None and p.value < n:
        prev = p
        p = p.next

    if p != None and p.value == n:
        return start

    q = Node(n)

    if prev == None:
        q.next = p
        return q

    prev.next = q
    q.next = p
    return start

    # [2] -> [3] -> [7] -> [11]

def print_all(p):
    while p != None:
        print(p.value, end = " ")
        p = p.next

z1 = insert(None,2)
z1 = insert(z1,3)
z1 = insert(z1,2)
z1 = insert(z1,7)
z1 = insert(z1,1)
z1 = insert(z1,5)

print_all(z1)