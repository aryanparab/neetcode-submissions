# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev= None
        nxt = head
        while nxt:
            temp = nxt.next
            nxt.next = prev
            prev = nxt
            nxt = temp
        return prev
            