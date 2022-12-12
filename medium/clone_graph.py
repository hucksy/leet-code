from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Node) -> Node:
    graph_dict = {}
    visit_que = deque()

    visit_que.append(node)
    while visit_que:
        cur_node = visit_que.pop()
        graph_dict[cur_node.val] = cur_node.neighbors
        for neighbor in cur_node.neighbors:
            if neighbor.val not in graph_dict:
                visit_que.appendleft(neighbor)

    return graph_dict[1]



