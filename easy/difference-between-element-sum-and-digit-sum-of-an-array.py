__author__ = 'meha001'
from typing import *

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = 0
        for i in  nums:
            s2 += sum(list(map(int, str(i))))
        return s1 - s2