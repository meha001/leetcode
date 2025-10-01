author = 'meha001'

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        kol = numBottles
        while numBottles:
            if numBottles < numExchange:
                numBottles = 0
                break
            else:
                kol += numBottles // numExchange
                numBottles = numBottles // numExchange + (numBottles % numExchange)
            
        return kol
    
print(Solution().numWaterBottles(15, 4))    
            