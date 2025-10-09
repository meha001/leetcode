__author__ = 'meha001'

from typing import *

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        t = []
        for i in order:
            if i in friends:
                t.append(i)
        return t
print(Solution().recoverOrder([3,1,2,5,4], [1,3,4]))