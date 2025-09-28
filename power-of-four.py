__author__ = 'meha001'
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bin(n)[2:].count('1') == 1 and bin(n)[2:].count("0") % 2 == 0 and n >= 0
    
print(Solution().isPowerOfFour(int(input())))