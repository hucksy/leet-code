from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head: Optional[ListNode]) -> bool:
    checked_nodes = []
    node = head

    while node.next is not None:
        if node.next in checked_nodes:
            return True
        else:
            checked_nodes.append(node)
            node = node.next

    return False