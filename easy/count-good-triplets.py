__author__ = 'meha001'

from typing import *

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        kol = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                        kol += 1
        return kol