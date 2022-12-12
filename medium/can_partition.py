from typing import List

def can_partition(nums: List[int]) -> bool:
    target = sum(nums) / 2

    if target % 2 != 0:
        return False

    def dfs(n: int, cur_sum: int):
        """
        do DFS on the tree to find a subset where sum == target
        n = level of tree, starting at length of nums
        cur_sum = tracking of sum towards the target
        """
        if cur_sum == target:
            return True
        if n == -1:
            return False
        return dfs(n-1, cur_sum) or dfs(n-1, cur_sum + nums[n])

    return dfs(len(nums)-1, 0)

n = [2]

print(can_partition(n))