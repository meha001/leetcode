__author__ = 'meha001'
from typing import *

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        t = []
        for i in range(len(s)):
            if s[i] == c:
                t.append(i)
                
        ans = []
        for i in range(len(s)):
            ans.append(min([abs(i-j) for j in (t)]))
            
        
        return ans
            