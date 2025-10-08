__author__ = 'meha001'

from typing import *

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        kol = 0
        t = nums[0]
        
        for i in range(1, len(nums)):
            t = t ^ nums[i]
            
        if t == 0:
            if len(set(nums)) == 1 and nums[0] == 0:
                return 0
            
            return len(nums) - 1
       
        if t != 0:
            return len(nums)
        
                
print(Solution().longestSubsequence([7, 6, 1, 9]))