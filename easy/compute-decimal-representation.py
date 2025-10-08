__author__ = 'meha001'
from typing import *

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        s = str(n)[::-1]
        t = []
        if s[0] != '0':
            t.append(int(s[0]))
            
        for i in range(1, len(s)):
            if s[i] != '0':
                
                t.append(int(s[i] + '0' * i))
                             
        return t[::-1]
    
print(Solution().decimalRepresentation(3000001))