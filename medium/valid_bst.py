from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    visit_que = deque()

    if not root:
        return False

    visit_que.appendleft(root)

    while visit_que:
        cur_node = visit_que.pop()
        if cur_node.left: 
            if cur_node.left.val >= cur_node.val:
                return False
            else:
                visit_que.appendleft(cur_node.left)

        if cur_node.right: 
            if cur_node.right.val <= cur_node.val:
                return False
            else:    
                visit_que.appendleft(cur_node.right)

    return True

"""
init visit_que and append root
    visit_que = root: val=0, left=None, right=None

enter while loop:
    cur_node: val=0, left=None, right=None
    visit_que = []


"""

print(None > 0)