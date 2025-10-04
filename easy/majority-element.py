__author__ = 'meha001'

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        t = dict()
        n = len(nums)
        for i in range(n):
            if f"{nums[i]}" in t:
                t[f"{nums[i]}"] = t[f"{nums[i]}"] + 1
            else:
                t[f"{nums[i]}"] = 1
            if n // 2 < t[f"{nums[i]}"]:
                return  nums[i]
            
print(Solution().majorityElement([3, 2, 3]))    