__author__ = 'meha001'
from typing import *

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        t = [0 for _ in range(num_people)]
        i = 0
        s = 0
        cd = 1
        while candies > 0:
            
            if i == num_people: i = 0
            # print(candies, cd)
            
            if (candies - cd) < 0:
                t[i] += candies
                candies -= cd
            
            
            else:
                t[i] += cd
                candies -= cd
                cd += 1
                
                
            
            i += 1
        return t
    
print(Solution().distributeCandies(10, 3))