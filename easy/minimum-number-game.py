__author = 'meha001'

from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        t = []
        while len(nums) != 0:
            s = nums[nums.index(min(nums))]
            nums.remove(s)
            
            s2 = nums[nums.index(min(nums))]
            nums.remove(s2)
            
            t.append(s2)
            t.append(s)
        return t
            