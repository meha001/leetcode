__author__ = 'meha001'

from typing import *

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        result = [1] * n  
        last_rain = {}  
        dry_days = []  
        
        for i in range(n):
            if rains[i] == 0:
                
                dry_days.append(i)
            else:
                lake = rains[i]
                result[i] = -1  
                
                if lake in last_rain:
                   
                    last_rain_day = last_rain[lake]
                    
                    
                    found = False
                    for j in range(len(dry_days)):
                        if dry_days[j] > last_rain_day:
                            
                            result[dry_days[j]] = lake
                            dry_days.pop(j)
                            found = True
                            break
                    
                    if not found:
                        return []  
                
                last_rain[lake] = i 
        
        return result


print(Solution().avoidFlood([69,0,0,0,69])) 