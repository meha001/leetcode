__author__ = 'meha001'
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.index(needle) if needle in haystack else -1
    
    
    
    
    
    
print(Solution().strStr(input(), input()))