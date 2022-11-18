from typing import List


def two_sum(num: List[int], target: int) -> List[int]:
    for i1, val in enumerate(num):
        for i2 in range((i1+1), len(num)):
            if num[i1] + num[i2] == target:
                return [i1, i2]


def two_sum_fast(nums: List[int], target: int) -> List[int]:
    """Returns a list containing the two indices of the inputted nums array which sum to the inputted target"""
    d = {}
    for i, num in enumerate(nums):
        num2 = target - num
        if num2 in d:
            return [d[num2], i]
        else:
            d[num] = i


nums = [2, 6, 11, 15, 7, 9]
print(two_sum(nums, 9))
print(two_sum_fast(nums, 9))
         