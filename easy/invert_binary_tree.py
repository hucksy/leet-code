from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:            
    if root:
        root.right, root.left = invertTree(root.left), invertTree(root.right)
        return root 


def factorial(n):
    if n == 1:
        return n
    return n * (factorial(n-1))

print(factorial(4))

