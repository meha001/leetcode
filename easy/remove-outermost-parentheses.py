__author__ = 'meha001'

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        k1 = 1
        k2 = 0
        tl = ''
        st = s[0]
        for i in range(1, len(s)):
            st += s[i]
            if s[i] == '(': k1 += 1
            if s[i] == ')': k2 += 1
            if k1 == k2 :
                tl += (st[1:-1])
                st = ''
                
        return tl
        
    
print(Solution().removeOuterParentheses("(()())(())(()(()))"))
            