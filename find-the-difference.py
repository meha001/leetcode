class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in s + t:
            if s+t.count(i) != 2:
                return i
        return ''
    