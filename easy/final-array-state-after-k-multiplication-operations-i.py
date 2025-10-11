__author__ = 'meha001'
from typing import *

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            t = nums.index(min(nums))
            
            nums[t] *= multiplier
        return nums