__author__ = 'meha001'

from typing import *


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        summa = 0
        nums = sorted(nums)
        
        for i in range(0, len(nums), +2):
            summa += nums[i]
        return summa
print(Solution().arrayPairSum([1, 4, 3, 2]))