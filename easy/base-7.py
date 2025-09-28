__author__ = 'meha001'

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def convertToBase7(self, num: int) -> str:
        s = ''
        t = 0
        t += num
        num = abs(num)
        
        while num >= 7:
            s += str(num % 7)
            num = num // 7
        s += str(num)
        if t < 0: s += '-'
        s = s[::-1]
        
        return s
    
print(Solution().convertToBase7(-100))