__author__ = 'meha001'
from typing import List
from collections import *
from itertools import *


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        kol = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if (sum(nums[:i]) - sum(nums[i:])) in [0, 1]:
                   kol += 1
                if (sum(nums[i:]) - sum(nums[:i])) in [0, 1]:
                   kol += 1
        return kol