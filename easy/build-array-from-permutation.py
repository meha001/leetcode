__author__ = 'meha001'

from typing import *

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        t = []
        
        for i in range(len(nums)):
            t.append(nums[nums[i]])

        return t            