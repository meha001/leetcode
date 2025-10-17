__author__ = 'meha001'
from typing import *

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = 0 + len(arr)
        while i < n:
            if arr[i] == 0:
                arr.insert(i, 0)
                i += 1
            i += 1
        
        while len(arr) != n:
            arr.pop()
        