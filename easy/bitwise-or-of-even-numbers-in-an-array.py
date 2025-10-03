__author__ = 'meha001'
import math 

class Solution:
    def evenNumberBitwiseORs(self, nums: list[int]) -> int:
        t = [(i) for i in nums if i % 2 == 0]
        if len(t) == 0:
            return 0
        
        t2 = []
        while len(t) != 1:
            t2 = []
            
            t2.append(t[0] | t[1])
            t.remove(t[0])
            t.remove(t[0])
            t = t2 + t
            t2 = []
            
        return t[0]
        
print(
    Solution().evenNumberBitwiseORs([1, 8, 16])
) 