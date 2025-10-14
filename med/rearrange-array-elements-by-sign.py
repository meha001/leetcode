__author__ = 'meha001'
from typing import *

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        t1 = []
        t2 = []
        for i in nums:
            if i > 0:
                t1.append(i)
            elif i < 0:
                t2.append(i)
        t = []
        for i in range(len(t1)):
            t.append(t1[i])
            t.append(t2[i])
        return t