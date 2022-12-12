from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: Optional[TreeNode]) -> bool:
    def get_height(root: Optional[TreeNode]):
        if root is None:
            return 0
        left = get_height(root.left)
        right = get_height(root.right)
        if left >= 0 and right >= 0 and abs(left - right) <= 1:
            return max(left, right) + 1
        else:
            return -1
    
    return get_height(root) != -1
