__author__ = 'meha001'
from typing import *


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        t = []
        s = 0
        for i in nums:
            s += i
            t.append(s)
        return t