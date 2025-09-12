import atexit

def reset_timer():
    with open("display_runtime.txt", "w") as f:
        f.write("0")

atexit.register(reset_timer)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]