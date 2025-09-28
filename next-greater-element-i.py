__author__ = 'meha001'

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        tlist = []
        for i in range(len(nums1)):
            flag = 0
            for j in range(nums2.index(nums1[i])+1, len(nums2)):
                if nums1[i] < nums2[j]:
                    tlist.append(nums2[j])
                    flag = 1
                    break
            if flag == 0:
                tlist.append(-1)
        return tlist
print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))