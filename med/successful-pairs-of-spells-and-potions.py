__author__ = 'meha001'

from typing import *

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() 
        n = len(potions)
        result = []
        
        for spell in spells:
            
            target = (success + spell - 1) // spell  
            
            
            left, right = 0, n - 1
            idx = n  
            
            while left <= right:
                mid = left + (right - left) // 2  
                
                if potions[mid] >= target:
                    idx = mid  
                    right = mid - 1  
                else:
                    left = mid + 1  
            
            result.append(n - idx)
        
        return result