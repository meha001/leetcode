__author__ = 'meha001'

from typing import *

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return -1
            
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        left_sorted = [True] * n
        for i in range(1, n):
            left_sorted[i] = left_sorted[i - 1] and nums[i] > nums[i - 1]
        
        right_sorted = [True] * n
        for i in range(n - 2, -1, -1):
            right_sorted[i] = right_sorted[i + 1] and nums[i] > nums[i + 1]
        
        left_unique = [True] * n
        seen = set()
        for i in range(n):
            if nums[i] in seen:
                left_unique[i] = False
            else:
                seen.add(nums[i])
                left_unique[i] = True
        
        right_unique = [True] * n
        seen = set()
        for i in range(n - 1, -1, -1):
            if nums[i] in seen:
                right_unique[i] = False
            else:
                seen.add(nums[i])
                right_unique[i] = True
        
        tmin = float('inf')
        
        for i in range(1, n):
            left_ok = (i == 1 or left_sorted[i - 1]) and left_unique[i - 1]
            right_ok = (i == n - 1 or right_sorted[i]) and right_unique[i]
            
            if left_ok and right_ok:
                left_sum = prefix_sum[i] - prefix_sum[0]
                right_sum = prefix_sum[n] - prefix_sum[i]
                diff = abs(left_sum - right_sum)
                if diff < tmin:
                    tmin = diff
        
        return int(tmin) if tmin != float('inf') else -1