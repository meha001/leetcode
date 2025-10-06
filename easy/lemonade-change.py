__import__ = 'meha001'

from typing import *

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        t5 = 0
        t10 = 0
        t20 = 0
        for i in bills:
            if i == 5:
                t5 += 1
            elif i == 10 and t5 != 0:
                t5 -= 1
                t10 += 1
            elif i == 20:
                if t5 >= 1 and t10 >= 1:
                    t5 -= 1
                    t10 -= 1
                elif t10 == 0 and t5 >= 3:
                    t5 -= 3
                
                else:
                    return False
            else:

                return False
            
        return True
    
print(Solution().lemonadeChange([5,5,10,10,20]))
