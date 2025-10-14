__author__ = 'meha001'

from itertools import *

from itertools import permutations

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def is_valid(candidate, pattern):
            for i in range(len(pattern)):
                if pattern[i] == 'I':
                    if candidate[i] >= candidate[i + 1]:
                        return False
                else:  # 'D'
                    if candidate[i] <= candidate[i + 1]:
                        return False
            return True
        
        n = len(pattern) + 1
        digits = [str(i) for i in range(1, n + 1)]
        
        for perm in permutations(digits):
            candidate = ''.join(perm)  
            if is_valid(candidate, pattern):
                return candidate
        
        return ""  