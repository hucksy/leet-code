import pprint as pp
from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    find distinct triplets within nums that sums to 0
    """
   
    pairs = []
    triplets = []


    for i1, val1 in enumerate(nums):
        for i2 in range(i1+1, len(nums)):
            if i1 != i2:
                p = sorted([(val1, i1), (nums[i2], i2)], key=lambda t: t[0])
                pairs.append(p)

    for i1, num in enumerate(nums):
        for i2, pair in enumerate(pairs):
                if i1 != pair[0][1] and i1 != pair[1][1]: 
                    trip = sorted([num, pair[0][0], pair[1][0]])
                    if sum(trip) == 0:
                        if trip not in triplets:
                            triplets.append(trip)
    
    return triplets


nums = [0,0,0]

print(three_sum(nums))
