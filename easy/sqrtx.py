__author__ = 'meha001'
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:return 0
        i = 2
        while i ** 2 <= x:
            i += 1
        return i - 1
    

print(Solution().mySqrt(100))