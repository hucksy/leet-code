from typing import List

def search(nums: List[int], target: int) -> int:
    start = 0
    stop = len(nums) - 1
    while stop > start:
        # check mid point higher/lower
        if target <= nums[(start + stop) // 2 ]:
            stop = (start + stop) // 2
        else:
            start = (start + stop) // 2 + 1
        
    if nums[start] == target:
        return start
    else:
        return -1    

nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(search(nums, target))