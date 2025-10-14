__author__ = 'meha001'

class Solution:
    def maxDepth(self, s: str) -> int:
        kol = 0
        tmax = float('-inf')
        for i in s:
            if i == '(':
                kol += 1
            elif i == ')':
                kol -= 1
            tmax = max(tmax, kol)
        return tmax