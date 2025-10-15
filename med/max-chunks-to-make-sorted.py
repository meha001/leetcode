__author__ = 'meha001'
from typing import *

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        k = 0
        for i in range(len(arr)):
            # print(arr[:i+1], i*(i+1)//2)
            if sum(arr[:i+1]) == i*(i+1)//2:
                k += 1
                
        return k