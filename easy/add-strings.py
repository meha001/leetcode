__author__ = 'meha001'
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        
        if len(num1) < len(num2):
            num1 = ['0'] * (len(num2) - len(num1)) + num1
        elif len(num1) > len(num2):
            num2 = ['0'] * (len(num1) - len(num2)) + num2
        
        result = ''
        carry = 0  
        
        for i in range(len(num1)-1, -1, -1):
            total = int(num1[i]) + int(num2[i]) + carry
            
            digit = total % 10
            carry = total // 10
            
            result = str(digit) + result
        
        if carry > 0:
            result = str(carry) + result
        
        return result


print(Solution().addStrings('456', '77'))  