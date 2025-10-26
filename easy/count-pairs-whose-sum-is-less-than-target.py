__author__ = 'meha001'
from typing import *
from collections import *
from itertools import *



class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        kol = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    kol += 1
        return kol