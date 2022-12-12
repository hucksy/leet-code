from typing import List

def majorityElement(nums: List[int]) -> int:
    count = 1
    x = nums[0]
    for i in range(1, len(nums)):
        if count == 0:
            count = 1
            x = nums[i]
        elif x == nums[i]:
            count += 1
        else:
            count -= 1
    return x
    
print(majorityElement([1]))
print(majorityElement([1,2,2,3,1,1,1,1]))
print(majorityElement([1,2,3,4,5,1,1,1,1,1,1,1]))

