__author__ = 'meha001'

from typing import *

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        max_len = 1
        current_len = 1
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1
                
        return max_len
                
print(Solution().findLengthOfLCIS([1,3,5,4,7]))