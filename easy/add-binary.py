__author__ = 'meha001'

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        t = int(a, 2)
        t2 = int(b, 2)
        return bin(t+t2)[2:]

print(Solution().addBinary('1010', '1011'))