__author__ = 'meha001'
from typing import *

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        delta = (sum_a - sum_b) // 2
        tb = set(bobSizes)
        
        for i in range(len(aliceSizes)):
            b = aliceSizes[i] - delta
            if b in tb:
                return [b, aliceSizes[i]] 