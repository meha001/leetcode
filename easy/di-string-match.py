__author__ = 'meha001'
from typing import *

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        t = [i for i in range(len(s) + 1)]
        t2 = []
        
        for i in range(len(s)):
            if s[i] == 'I':
                t2.append(t[0])
                t.remove(t[0])
                
            if s[i] == 'D':
                t2.append(t[- 1])
                t.remove(t[-1])
                
        if s[-1] == 'D':
            t2.append(t[0])
        else:
            t2.append(t[-1])
        return t2
    
print(Solution().diStringMatch('III'))

