__author__ = 'meha001'

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        tlist = [i for i in range(1, len(nums) + 1)]
        for i in range(len(nums)):              
                tlist[nums[i] - 1] = 0 - abs(tlist[nums[i] - 1])
                
        return [i for i in tlist if i > 0]
    
    
    
print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))