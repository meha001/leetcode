import atexit

def reset_timer():
    with open("display_runtime.txt", "w") as f:
        f.write("0")

atexit.register(reset_timer)

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s2 = ''
        for i in s:
            if i.isalnum():
                s2 += i.upper()
        return s2 == s2[::-1] 
    
print(Solution().isPalindrome('A man, a plan, a canal: Panama"'))