__author__ = 'meha001'

from typing import *
from bisect import *

class Solution:
    def maxFrequency(self, nums: List[int], k: int, operations: int) -> int:
        
        sorted_nums = sorted(nums)
        frequency_counter = Counter(sorted_nums)
        
        max_frequency = 0
        
        for target_value in range(sorted_nums[0], sorted_nums[-1] + 1):
            left_bound = bisect_left(sorted_nums, target_value - k)
            right_bound = bisect_right(sorted_nums, target_value + k)
            
            convertible_count = right_bound - left_bound
            
            current_frequency = frequency_counter.get(target_value, 0)
            
            additional_elements = min(
                convertible_count - current_frequency,  
                operations  
            )
            
            total_frequency = current_frequency + additional_elements
            max_frequency = max(max_frequency, total_frequency)
        
        return max_frequency