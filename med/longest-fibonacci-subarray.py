__author__ = 'meha001'
from typing import *


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
      
        
        n = len(nums)
        if n <= 2:
            return n

        max_len = 2
        curr_len = 2

        for i in range(2, n):
            if nums[i] == nums[i - 1] + nums[i - 2]:
                curr_len += 1
            else:
                curr_len = 2
            max_len = max(max_len, curr_len)

        return max_len
