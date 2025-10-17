__author__ = 'meha001'

from typing import *

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        t = []
        
        for i in range(1, len(arr)):
            
            t.append(arr[i-1] - arr[i])
        return len(set(t)) == 1