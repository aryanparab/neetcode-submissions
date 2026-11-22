import heapq
class MinStack:

    def __init__(self):
        self.hp = []
        self.st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        heapq.heappush(self.hp,val)

    def pop(self) -> None:
        x = self.st.pop(-1)
        if x==self.hp[0]:
            heapq.heappop(self.hp)

    def top(self) -> int:
        return self.st[-1]
    def getMin(self) -> int:
        return self.hp[0]
