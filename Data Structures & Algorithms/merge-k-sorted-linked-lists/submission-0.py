# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap =[]
        d = {}
        head = ListNode()
        ans =head
        
        for llist in lists:
            while llist:
                if llist.val in d:
                    d[llist.val].append(llist)
                else:
                    heapq.heappush(heap,(llist.val))
                    d[llist.val] = [llist]
                llist = llist.next
        while heap:
            v= heapq.heappop(heap)
            while d[v]:
                x = d[v].pop(0)
                ans.next = x
                ans = ans.next
        ans.next = None
        return head.next