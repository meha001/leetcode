__author__ = 'meha001'

from typing import *

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        t = ([i for i in range(len(nums)) if sum(nums[:i]) == sum(nums[i+1:])])
        if t:
            return (min(t))
        else:
            return (-1)