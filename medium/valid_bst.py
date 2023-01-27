import math
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_validBST(root: Optional[TreeNode]) -> bool:

    def validate(node: TreeNode, low=-math.inf, high=math.inf):
        if not node:
            return True

        if node.val <= low or node.val >= high:
            return False
        
        return (validate(node.left, low=low, high=node.val) and
            validate(node.right, low=node.val, high=high))

    return validate(root)



two = TreeNode(2, None, None)
six = TreeNode(6, None, None)
five = TreeNode(5, two, six)
nine = TreeNode(9, None, None)
fifteen = TreeNode(15, nine, None)
root = TreeNode(10, five, fifteen)

print(is_validBST(root))