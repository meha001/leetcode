__author__ = 'meha001'
from typing import *


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # kol = 0
        t = []
        for i in range(len(nums)):
            kol = 0
            for j in range(len(nums)):
                kol += (i != j) and (nums[i] > nums[j])
            t.append(kol)
        return t