__author__ = 'meha001'
from typing import *

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        t = float('inf')
        for i in range(len(list1)):
            if list1[i] in list2:
                
                if i + list2.index(list1[i]) < t:
                    s = [list1[i]]
                    t = i + list2.index(list1[i])
                    
                elif i + list2.index(list1[i]) == t:
                    s.append(list1[i])
        return s