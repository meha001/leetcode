__author__ = 'meha001'

class RecentCounter:

    def __init__(self):
        self.requests = []  
        
    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        lower_bound = t - 3000
        
        while self.requests and self.requests[0] < lower_bound:
            self.requests.pop(0)
        
        return len(self.requests)
