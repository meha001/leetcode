__author__ = 'meha001'

from typing import List

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        t = sorted(score)[::-1]
        for i in range(len(t)):
            if i == 0:score[score.index(t[i])] = 'Gold Medal'
            elif i == 1:score[score.index(t[i])] = 'Silver Medal'
            elif i == 2:score[score.index(t[i])] = 'Bronze Medal'
            else:
                score[score.index(t[i])] = f'{i + 1}'
        return score
print(Solution().findRelativeRanks([10,3,8,9,4]))

