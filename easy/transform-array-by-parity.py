__author__ = 'meha001'

from typing import *

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        s = []
        for i in nums:
            if i % 2 == 0:
                s.insert(0, 0)
            else:
                s.append(1)
        return s