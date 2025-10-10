__author__ = 'meha001'

from typing import *

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum([abs(s.index(t[i]) - s.index(s[i])) for i in range(len(s))])