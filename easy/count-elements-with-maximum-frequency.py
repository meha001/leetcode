__author__ = 'meha001'
from typing import *
from collections import *
from itertools import *

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        t = []
        s = sorted(list(set(nums)))
        nums = sorted(nums)
        for i in s:
            t.append(nums.count(i))
        print(t)
        t2 = sorted(list(set(t)))
        t = sorted(t)
        t3 = []
        for i in t2:
            t3.append(t.count(t2))
            
        return max(t3)