class Solution:
    def smallestNumber(self, n: int) -> int:
        for i in range(n, 9999999999999):
            if '0' not in bin(i)[2:]:
                return i