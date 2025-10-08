__author__ = 'meha001'

from typing import *

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        s = 1
        summ = 0
        for i in range(len(nums)):
            summ += s * nums[i]
            print(summ, s)
            s = -s
        print(summ)
    
(Solution().alternatingSum([1,3,5,7]))