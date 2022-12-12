from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    level_list = []
    visited = deque([])

    if root:
        visited.append((root, 1))
        while visited:
            cur_node = visited.popleft()
            cur_val = cur_node[0].val
            level = cur_node[1]

            if len(level_list) is None or level > len(level_list):
                level_list.append([cur_val])
            else:
                level_list[level-1].append(cur_val)

            if cur_node[0].left:
                visited.append((cur_node[0].left, cur_node[1]+1))
            if cur_node[0].right:
                visited.append((cur_node[0].right, cur_node[1]+1))

    return level_list

node_9 = TreeNode(9)
node_15 = TreeNode(15)
node_7 = TreeNode(7)
node_20 = TreeNode(20, node_15, node_7)
root = TreeNode(3, node_9, node_20)

lo_list = level_order(root)
print(lo_list)
