# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        
        while node  and node.next:
            n1,n2 = node.val,node.next.val
            while n1!=n2:
                if n1>n2:
                    n1-=n2
                else:
                    n2-=n1
            nn=ListNode(n1)
            nxt = node.next
            node.next = nn
            nn.next = nxt
            node = nxt
        return head