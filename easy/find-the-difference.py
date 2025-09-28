__author__ = 'meha001'
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return [i for i in t if s.count(i) != t.count(i)][0]