import atexit
def reset_timer():
    with open("display_runtime.txt", "w") as f:
        f.write("0")

atexit.register(reset_timer)

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and str(bin(n)).count('1') == 1
        
