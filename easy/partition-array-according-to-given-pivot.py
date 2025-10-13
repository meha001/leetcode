__author__ = 'meha001'

from typing import *

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        t1 = []
        t2 = []
        t3 = []
        tlist = []
        for i in range(len(nums)):
            if nums[i] > pivot:
                t2.append(nums[i])
                
            if nums[i] < pivot:
                t1.append(nums[i])
                
            if nums[i] == pivot:
                t3.append(nums[i])
        
        
        return t1+t3+t2