__author__ = 'meha001'

from typing import *

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        t = list(set(nums))
        kol = -1
        maxims = []
        for i in t:
            maxims.append(nums.count(i))
        
        tmax = max(maxims)
        tindexes = []
        
        for i in range(len(maxims)):
            if maxims[i] == tmax:
                tindexes.append(i)
        print(tindexes)
        tmin = 99999999
            
        for i in range(len(tindexes)):
            
            
            flag = -1
            ind1 = 0
            ind2 = 0
            
            for j in range(len(nums)):
                if nums[j] == t[tindexes[i]] and flag == -1:
                    ind1 = j
                    flag = 0
                
                if nums[j] == t[tindexes[i]] and flag != -1:
                    ind2 = j
            
            if (ind2 - ind1) < tmin:
                tmin = ind2 - ind1 + 1
                
        return tmin
                    
                    
    
print(Solution().findShortestSubArray([1, 2]))

nums = 12245
t = 1245
maxims = 1211
tmax = 2
tindexes = 1
