__author__ = 'meha001'
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(a):
    return a >= 4

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:return 1
        left = 1
        right = n
        while left < right:
            mid = (right + left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
            
        return left
    
        
print(Solution().firstBadVersion(5))