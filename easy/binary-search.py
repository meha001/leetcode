__author__ = 'meha001'

from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                
            elif nums[mid] > target:
                right = mid - 1
            
            
        return -1
print(Solution().search([-1,0,3,5,9,12], 9))