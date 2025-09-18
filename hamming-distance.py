class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        kol = 0
        if len(x) < len(y):
            x = ('0' * (len(y) - len(x))) + x
        elif len(x) > len(y):
            y = ('0' * (len(x) - len(y))) + y
         
        for i in range(min(len(x), len(y))):
            if x[i] != y[i]:
                kol += 1 
        return kol
print(Solution().hammingDistance(3, 1))