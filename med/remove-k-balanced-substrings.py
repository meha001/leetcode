__author__ = 'meha001'

from typing import *

class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        st = '(' * k +  ')' * k
        
        while st in s:
            s = s.replace(st, '')
            
        return s
    

print(Solution().removeSubstring("((()))()()()", k = 3))