__author__ = 'meha001'

class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        t = []
        while len(nums) != 1:
            t = []
            for i in range(len(nums)-1):
                t.append((nums[i] + nums[i+1]) % 10)
            
            nums.clear()
            nums += t
            print(nums)
        else:
            return nums[0]

print(Solution().triangularSum([5]))