__author__ = 'meha001'

from typing import *

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        s = 0
        for i in nums:
            s += i if nums.count(i) % k == 0 else 0
        
        return s