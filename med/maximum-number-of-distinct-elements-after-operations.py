__author__ = 'meha001'

from typing import *

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        tlast = float('-inf')
        nums = sorted(nums)
        st = set()
        for i in range(len(nums)):
            tlstar = max(tlast + 1, nums[i] - k)
            tlend = nums[i] + k
            
            if (tlstar <= tlend):
                st.add(tlstar)
                tlast = tlstar
                
        return st

print(Solution().maxDistinctElements([1,2,2,3,3,4], 2))