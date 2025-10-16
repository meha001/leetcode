__author__ = 'meha001'
from typing import *

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = {}
        for num in nums:
            r = num % value
            freq[r] = freq.get(r, 0) + 1

        mex = 0
        while True:
            r = mex % value
            if freq.get(r, 0) > 0:
                freq[r] -= 1
                mex += 1
            else:
                return mex