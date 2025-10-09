__author__ = 0
from typing import *

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        kol = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    kol += 1
                    
        return kol
