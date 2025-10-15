__author__ = 'meha001'
import math
from typing import *

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        kol = 100
        tk = 1
        for i in range(len(s)):
            
            if kol - widths[ord(s[i]) - 97] < 0:
                tk += 1
                kol = 100
                
            kol -= widths[ord(s[i]) - 97]
            
        return [tk, 100-kol]