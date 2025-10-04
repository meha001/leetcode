__author__ = 'meha001'

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        t = [[1], [1, 1]]
        if numRows == 1:return [t[0]]
        elif numRows == 2: return t
        else:
            while len(t)-1 != numRows:
                tlis = [1]
                for i in range(len(t[-1])-1):
                    tlis.append(t[-1][i] + t[-1][i+1])
                tlis.append(1)
                t.append(tlis)
            return t[-1]

print(Solution().generate(3))

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
