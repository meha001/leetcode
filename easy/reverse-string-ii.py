__author__ = 'meha001'

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        strings = []
        flag = 0
        st = ''
        
        for i in range(len(s)):
            if flag != k * 2:
                flag += 1
                st += s[i]
            else:
                strings.append(st)
                st = s[i]
                flag = 1
                
        if flag != 0:
            strings.append(st)
        # print(strings)/
        
        srs = ''
        for i in range(len(strings)):
            sr = ''
            if k <= len(strings[i]):
                for j in range(k):
                    sr += strings[i][j]
                sr = sr[::-1]
                sr += strings[i][k:]
                srs += sr
            else:
                srs += strings[i][::-1]
        return (srs)
            

# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         name = list(s)
#         for i in range(0,len(name),2*k):
#             name[i:i+k] = reversed(name[i:i+k])
#         s = "".join(name)
#         return s

print(Solution().reverseStr("abcdefg", 8))
