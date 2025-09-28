__author__ = 'meha001'

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                elif image[i][j] == 1:
                    image[i][j] = 0
        return image

print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))