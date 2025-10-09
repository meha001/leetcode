__author__ = 'meha001'

from typing import *

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(list(set(nums)))[::-1]
        return nums[:k]
print(Solution().maxKDistinct(nums = [84,93,100,77,90], k = 3))
        