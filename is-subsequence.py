class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = (list(s))
        t = (list(t))
        for i in t:
            if len(s) != 0:
                if i == s[0]:
                    s.remove(s[0])
        if len(s) == 0:
            return True
        else:
            return False
print(Solution().isSubsequence('abc', 'ahbgdc'))