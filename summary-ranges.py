class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        t = []
        sart = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if sart == nums[i-1]:
                    t.append(str(sart))
                else:t.append(f"{sart}->{nums[i-1]}")
                sart = nums[i]
        if sart == nums[-1]:
            t.append(str(sart))
        else:
            t.append(f"{sart}->{nums[-1]}")
            
        return t