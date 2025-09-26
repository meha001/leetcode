__author__ = 'meha001'

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed
        flowerbed.append(0)
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                if n == 0: return True
                else:
                    n -= 1
                    flowerbed[i] = 1
        return n == 0
print(Solution().canPlaceFlowers([1,0,0,0,1], 2))