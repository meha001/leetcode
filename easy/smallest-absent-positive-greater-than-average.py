__author__ = 'meha001'
 
from typing import *

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        tmid = (sum(nums) // len(nums)) + 1
        while 1:
            if tmid not in nums and tmid > 0:
                return tmid
            tmid += 1
        
        return tmid
    
print(Solution().smallestAbsent(nums =[3,5]))