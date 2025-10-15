__author__ = 'meha001'
from typing import *

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        summ = 0
        for i in range(len(arr)):
            t = []
            for j in range(i, len(arr)):
                
                t.append(arr[j])
                if len(t) % 2:
                    summ += sum(t)
        return summ                