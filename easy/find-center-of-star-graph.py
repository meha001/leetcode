__author__ = 'meha001'

from typing import *

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        f = 0
        t = edges[0][f]
        for i in edges:
            if t not in i:        
                f = 1
                break
        t = edges[0][f]
        return t
    
print(Solution().findCenter([[1,2],[5,1],[1,3],[1,4]]))