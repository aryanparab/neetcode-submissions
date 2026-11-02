"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        root = head
        mp = {None:None}
        while root:
            mp[root]= Node(root.val)
            root= root.next
        root = head
        while root:
            mp[root].next = mp[root.next]
            mp[root].random = mp[root.random]
            root= root.next
        return mp[head]
        