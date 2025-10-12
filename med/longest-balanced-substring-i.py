__author__ = 'meha001'
from collections import *

class Solution:
    def longestBalanced(self, s: str) -> int:
        tmax = 0
        n = len(s)
        
        for i in range(n):
            freq = Counter()
            for j in range(i, n):
                freq[s[j]] += 1
                values = list(freq.values())
                if max(values) == min(values):
                    tmax = max(tmax, j - i + 1)
        return tmax

                
print(Solution().longestBalanced("hhgh"))
print(Solution().longestBalanced("abbac"))
print(Solution().longestBalanced("zzabccy"))
print(Solution().longestBalanced("aba"))
