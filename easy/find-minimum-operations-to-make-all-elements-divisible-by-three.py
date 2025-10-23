__author__ = 'meha001'
from typing import *

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        kol = 0
        for i in nums:
            if i % 3 == 2:
                kol += 1
            if i % 3 == 1:
                kol += 1
            
        return kol