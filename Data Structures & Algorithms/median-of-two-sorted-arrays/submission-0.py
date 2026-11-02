import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        hp = []
        for i in nums1:
            heapq.heappush(hp,i)
        for j in nums2:
            heapq.heappush(hp,j)
        temp = []
        while hp:
            temp.append(heapq.heappop(hp))
        l = len(temp)
        print(temp)
        if l%2==0:
            return (temp[l//2-1] + temp[l//2])/2
        else:
            return temp[l//2]