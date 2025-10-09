__author__ = 'meha001'

class Solution:
    def concatHex36(self, n: int) -> str:
        def to_base(num: int, base: int) -> str:
            if num == 0:
                return "0"
                
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""
            
            while num > 0:
                result = digits[num % base] + result
                num //= base
                
            return result
        
        n2 = n ** 2
        n3 = n ** 3
        
        hex_part = to_base(n2, 16)
        
        base32_part = to_base(n3, 36)
        
        return hex_part + base32_part

# Test the function
print(Solution().concatHex36(36)) 