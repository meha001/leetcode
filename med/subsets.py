__author__ = 'meha001'
from typing import *
from collections import *
from itertools import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        t = [[]]
        for i in range(1, len(nums)+1):
            for j in combinations(nums, i):
                t.append(j)
        return t