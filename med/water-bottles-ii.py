__author__ = 'meha001'

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ButtleDrunk = 0
        emptyBottles = 0
        
        while numBottles:
            ButtleDrunk += numBottles
            numBottles -= numExchange
            numExchange += 1
            
        return ButtleDrunk
print(Solution().maxBottlesDrunk(13, 6))