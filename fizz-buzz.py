__author__ = 'meha001'
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        t = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                t.append("FizzBuzz")
            elif i % 3 == 0 and i % 5 != 0:
                t.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                t.append("Buzz")
            else:
                t.append(f"{i}")
        return t