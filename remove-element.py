__author__ = 'meha001'
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Безопасное удаление (но неэффективное)
        k = len(nums) - nums.count(val)
        i = 0
        while len(nums):
            f = 0
            for i in range(len(nums)):
                if nums[i] == val:
                    nums.remove(nums[i])
                    f = 1
                    break
            if f == 0:
                break    
        return k 
                    
                     
print(Solution().removeElement([1, 2, 3], 2))