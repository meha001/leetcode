__author__ = 'meha001'

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        s1 = 'qwertyuiop'
        s2 = 'asdfghjkl'
        s3 = 'zxcvbnm'
        tlist = []
        for i in range(len(words)):
            flag = 0
            s = '' + words[i]
            words[i] = words[i].lower()
            for j in range(len(words[i])):
                if words[i][j] in s1:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 0:
                for j in range(len(words[i])):
                    if words[i][j] in s2:
                        flag = 1
                    else:
                        flag = 0
                        break
            if flag == 0:
                for j in range(len(words[i])):
                    if words[i][j] in s3:
                        flag = 1
                    else:
                        flag = 0
                        break
            if flag:
                tlist.append(s)
        return tlist
print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))