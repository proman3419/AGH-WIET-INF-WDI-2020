def singleton(head):
    curr = head
    prev = None

    while curr is not None:
        curr1 = curr.next
        prev1 = curr
        remove1 = False
        
        while curr1 is not None:
            if curr.value == curr1.value:
                prev1.next = curr1.next
                curr1 = curr1.next
                remove1 = True
            else:
                prev1, curr1 = curr1, curr1.next
        
        if remove1:
            if prev is None:
                head = head.next
            else:
                prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return head