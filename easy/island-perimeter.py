__author__ = 'meha001'
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        summa = 0
        tlist = [[0] * (len(grid[-1])+2)]
        for i in range(len(grid)):
            tlist.append([0]+grid[i] + [0])
            
        tlist.append((len(grid[-1])+2)*[0])
        
        for i in range(len(tlist)):
            for j in range(len(tlist[i])):
                if tlist[i][j] == 1:
                    if tlist[i][j-1] == 0:
                        summa += 1
                    if tlist[i-1][j] == 0:
                        summa += 1
                    if tlist[i+1][j] == 0:
                        summa += 1
                    if tlist[i][j+1] == 0:
                        summa += 1
                            
        return summa
print(Solution().islandPerimeter([[1,0]]))