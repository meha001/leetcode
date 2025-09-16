class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """       
        if num == 0:
            return "0"
        
        
        if num < 0:
            num = (1 << 32) + num
        
        t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']
        if num < 0:
            num = abs(num)
        ls = []
        while num >= 16:
            ls.append(num % 16)
            num = num // 16
        ls.append(num % 16)
        ls = ls[::-1]
        s = ''
        for i in ls:
            s += str(t[i])
        return s
        
        
