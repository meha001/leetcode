class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        # """
        if len(s) % 2 == 1:
            return False
        while len(s) != 0:
            if '[]' in s:
                s = s[:s.index('[]')] + s[s.index('[]')+2:] 
            elif '()' in s:
                s = s[:s.index('()')] + s[s.index('()')+2:] 
            elif '{}' in s:
                s = s[:s.index('{}')] + s[s.index('{}')+2:] 
            else:
                return False            
        return True
print(Solution().isValid(input()))