__author__ = 'meha001'


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        tlist = ''
        while columnNumber > 0:
            columnNumber -= 1
            
            remainder = columnNumber % 26
            tlist += chr(65 + remainder)  
            columnNumber //= 26
            
        return tlist[::-1]
        
       
    
print(Solution().convertToTitle(3))