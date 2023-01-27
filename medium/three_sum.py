import pprint as pp
from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    find distinct triplets within nums that sums to 0
    """
   
    triplets = []
    nums.sort()

    # i, num - loop through nums:
        # skip repeated values to avoid duplicates
        # two_sum(i, nums, triplets)


def two_sum(i: int, nums: List[int], triplets: List[int]):
    d = {}

    j = i + 1
    for j, num in enumerate(nums):
        target = -nums[i] - nums[j]
        if n2 in d:
            return [d[n2], i]
        else:
            d[num] = i
    

nums = [1,2,3,4,-4,0,-2]

nums = [-4,-2,0,1,2,3,4]



print(three_sum(nums))
