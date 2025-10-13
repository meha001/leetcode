__author = 'meha001'

from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        kol = 0
        i = 0
        while  tickets[k] != 0:
            kol += 1
            if tickets[i] <= 0: 
                kol -= 1
            
            tickets[i] -= 1
            
            i += 1
            if i == len(tickets):
                i = 0
        return kol
            
print(Solution().timeRequiredToBuy([2,3,2], 2)) 