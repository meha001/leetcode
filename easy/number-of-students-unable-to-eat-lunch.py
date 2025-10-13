__author__ = 'meha001'

from typing import *

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:          
        i = 0
        while len(students) and i != len(students):    
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                i = 0
            else:
                students.append(students[0])
                students.pop(0)
                i += 1
        
        if i == len(students):
            return i
print(Solution().countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))