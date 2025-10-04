__author__ = 'meha001'
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        tmax = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                tmax = max(tmax, (sell - buy))
            else:
                buy = sell
                
        return tmax
    
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))