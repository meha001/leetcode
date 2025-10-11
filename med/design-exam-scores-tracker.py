__author__ = 'meha001'

import bisect
        
class ExamTracker:

    def __init__(self):
        self.times = []
        self.prefix = [0] 

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.prefix.append(self.prefix[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        glavonitre = (startTime, endTime)
        
        left = bisect.bisect_left(self.times, startTime)
        right = bisect.bisect_right(self.times, endTime)

        return self.prefix[right] - self.prefix[left]



# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)
