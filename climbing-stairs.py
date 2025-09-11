class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [1, 1, 2]
        for _ in range(n):
            t.append(t[-1] + t[-2])
        return t[n]
    
print(Solution().climbStairs(2))