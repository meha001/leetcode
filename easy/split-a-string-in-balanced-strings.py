__author__ = 'meha001'
from typing import *

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        kol = 0
        k = 0
        for i in s:
            k += 1 if i == 'L' else -1
            if k == 0:
                kol += 1
        return kol