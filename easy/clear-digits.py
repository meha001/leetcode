__author__ = 'meha001'

class Solution:
    def clearDigits(self, s: str) -> str:
        t2 = [s[0]]
        
        ks = []
        if s[0].isalpha():
            ks.append(0)
        
        for i in range(1, len(s)):
            print(ks)
            if s[i].isalpha():
                ks.append(i)
                t2.append(s[i])
                
            elif s[i].isdigit() and len(ks) != 0:
                t2.pop()
                ks.pop()
            
            elif s[i].isdigit() and len(ks) == 0:
                t2.append(s[i])

            
        return ''.join(t2)    
            
print(Solution().clearDigits("cb34"))