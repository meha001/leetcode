__author = 'meha001'

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))[::-1]
        if len(nums) < 3:
            return nums[0]
        else:
            return nums[2]