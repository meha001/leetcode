__author__ = 'meha001'

from typing import *

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        t = []
        for i in range(len(prices)):
            f = 0
            
            for j in range(i + 1, len(prices)):
            
                if prices[i] > prices[j]:
                    t.append(prices[i] - prices[j])
                    f = 1
                    break
                
            if f == 0:
                t.append(prices[i])
                
        return t