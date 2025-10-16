__author__ = 'meha001'
from typing import *

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t = [0 for i in s]
        
        for i in range(len(indices)):
            t[indices[i]] = s[i]
        return ''.join(t)