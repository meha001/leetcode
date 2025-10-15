__author__ = 'meha001'

from typing import *

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        kol, precnt, tmax = 1, 0, 0
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                kol += 1
            else:
                precnt = kol
                kol = 1
            tmax = max(tmax, min(precnt, kol))
            tmax = max(tmax, kol // 2)
        
        return tmax
        
print(Solution().maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7]))