import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        heap = []
        n = len(hand)
        if groupSize<2:return True
        for i in range(n):
            heapq.heappush(heap,hand[i])
        while heap :
            x =[]
            x.append( heapq.heappop(heap))
            addback = []
            while heap and len(x)<groupSize:
                while heap and x[-1]==heap[0]:
                    addback.append(heapq.heappop(heap))
                # if not heap:return False
                if not heap or heap[0]-x[-1]!=1:return False
                x.append(heapq.heappop(heap))
            if len(x)!=groupSize:
                return False
            for i in addback:
                heapq.heappush(heap,i)

        return True

