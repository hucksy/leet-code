from typing import List

def max_subArray(nums: List[int]) -> int:
    max_tally = nums[0]
    tally = 0
    for i, val in enumerate(nums):
        tally += val
        max_tally = max(tally, max_tally)
        tally = max(max_tally, 0)

    return max_tally


nums = [-2,1,-3,4,-1,2,1,-5,4]

print(max_subArray(nums))