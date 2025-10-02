__author__ = 'meha001'

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ButtleDrunk = numBottles
        emptyBottles = 0
        
        while numBottles - numExchange >= 0:
            ButtleDrunk += 1
            numBottles -= numExchange
            numExchange += 1
            numBottles += 1
            
        return ButtleDrunk
    
print(Solution().maxBottlesDrunk(13, 6))