__author__ = 'meha001'

from typing import *

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
    
        freq = Counter(s)
        
        groups = {}
        for char, count in freq.items():
            groups.setdefault(count, []).append(char)
        
        best_group = max(groups.items(), key=lambda x: (len(x[1]), x[0]))
        
        return ''.join(best_group[1])
        
Solution().majorityFrequencyGroup('aaabbbccdddde')