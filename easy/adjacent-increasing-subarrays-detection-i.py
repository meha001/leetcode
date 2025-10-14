__author__ = 'meha001'

from typing import *

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
            def sort(t):
                for i in range(len(t)-1):
                    if t[i] >= t[i+1]:
                        return False
                return True
            
            for i in range(len(nums)):
                t = []
                if len(nums) - (i + k) >= 0:
                    for j1 in range(i, i + k):
                        t.append(nums[j1])
                
                if sort(t) and len(nums) - (i + k + k) >= 0:
                    t2 = []
                    for j2 in range(i + k, i + k + k):
                        t2.append(nums[j2])
                    # print(t2)
                    if sort(t2) and len(t) == len(t2):
                        print(t, t2)
                        return True

            return False
        
print(Solution().hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7], 5))