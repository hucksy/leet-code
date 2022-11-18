from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i, val in intervals:
            if newInterval[0] < val[0]:
                val[0] = newInterval[0]
            elif newInterval[0] > val[0]

list1 = [[1,3],[6,9]]
new_interval1 = [2,5]
list2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval2 = [4,8]