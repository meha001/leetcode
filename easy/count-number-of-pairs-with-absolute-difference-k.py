__author__ = 'meha001'
from typing import *

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        kol = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    kol += 1
        return kol 