from typing import *

__author__ = 'meha001'

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        return sorted(nums)
    