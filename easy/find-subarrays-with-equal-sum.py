__author__ = 'meha001'
from typing import *

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        seen_sum = set()

        for i in range(n-1):
            pair_sum = nums[i] + nums[i+1]

            if pair_sum in seen_sum:
                return True
            
            seen_sum.add(pair_sum)


        return False