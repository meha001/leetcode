__author__ = 'meha001'
from typing import List
from collections import *
from itertools import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums, len(nums)-1))