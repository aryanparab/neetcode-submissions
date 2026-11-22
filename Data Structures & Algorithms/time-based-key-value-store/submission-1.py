import heapq
class TimeMap:

    def __init__(self):
        self.d ={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.d:
            self.d[key] = []
        heapq.heappush(self.d[key],[-1*timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        temp = []
        ans = ""
        curr = self.d.get(key,[])
        while curr and ans =="":
            x = heapq.heappop(curr)
            if -1*x[0] <= timestamp:
                ans = x[1]
            temp.append(x)
        for i in temp:
            heapq.heappush(curr,i)
        self.d[key] = curr
        return ans
        
