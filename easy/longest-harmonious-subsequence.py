__author__ = 'meha001'

from typing import *

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        freq = Counter(nums)
        print(freq)
        
        if len(freq) == 1: return 0
        maxLen = 0
        for x, f in freq.items():
            if x-1 in freq:
                maxLen = max(maxLen, f + freq[x-1])
        return maxLen

Solution().findLHS([1,3,2,2,5,2,3,7])