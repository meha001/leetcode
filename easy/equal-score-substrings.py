__author__ = 'meha001'

from typing import *

class Solution:
    def scoreBalance(self, s: str) -> bool:
        n = len(s)
        
        t = [0 for i in range(n)]
        t[0] = ord(s[0]) - 96
        
        for i in range(1, n):
            t[i] = (ord(s[i]) - 96)
            
        flag = 0
        for i in range(n):
            if sum(t[:i]) == sum(t[i:]):
                flag = 1
                
        return bool(flag)
    
print(Solution().scoreBalance("bace"))