__author__ = 'meha001'
from typing import *

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        kol = 0
        for i in words:
            f = 1
            for j in i:
                if j not in allowed:
                    f = 0
                    break
            if f:kol+=1
        return kol