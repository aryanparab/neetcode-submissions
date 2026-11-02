import heapq
class TimeMap:

    def __init__(self):
        self.d ={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.d:
            self.d[key] = []
        self.d[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
   
        ans = ""
        curr = self.d.get(key,[])
        
        low = 0
        high = len(curr) - 1
        ans = -1 

        while low <= high:
            mid = low + (high - low) // 2

            if curr[mid][0] <= timestamp:
                ans = mid    
                low = mid + 1 
            else:
                high = mid - 1 

        return "" if ans==-1 else curr[ans][1]  