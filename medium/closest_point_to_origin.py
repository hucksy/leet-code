from collections import deque
from typing import List
import math
import bisect

def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    closest = []

    for i, coord in enumerate(points):
        distance = math.sqrt(coord[0] ** 2 + coord[1] ** 2)
        bisect.insort(closest, [distance, coord[0], coord[1]], key= lambda point: point[0])
    return [point[1:3] for point in closest[:k]]




points = [[3,3],[5,-1],[-2,4]]
k = 2
print(k_closest(points=points, k=k))