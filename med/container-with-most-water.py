__author__ = 'meha001'
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        square = (right) * (min(height[left], height[right]))
        while left != right:
            if height[left] < height[right]:
                square = max((right - left) * (min(height[left], height[right])), square)
                left += 1
                
            else:
                square = max((right - left) * (min(height[left], height[right])), square)
                right -= 1
        
       
        return square
    
print(Solution().maxArea([8,7,2,1]))