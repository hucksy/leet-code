from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    next = None
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev

    
c = ListNode(3, None)
b = ListNode(2, c)
a = ListNode(1, b)

reversed = reverseList(a)
print(reversed.val)
print(reversed.next.val)