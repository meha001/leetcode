__author__ = 'meha001'

from typing import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        summ = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                
                summ += nums[i-1] - nums[i] + 1
                nums[i] = nums[i] + (nums[i-1] - nums[i] + 1)
        return summ
                