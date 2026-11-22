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
        mp = {}
        i =0 
        while root:
            mp[i]= Node(root.val)
            root = root.next
            i+=1
        root = head
        j= 0
        while root:
            current = mp[j]
            if root.next:
                for i in mp.keys():
                    if root.next.val == mp[i].val:
                        current.next= mp[i]
                        break
            if root.random:
                f = root.random.val
                for i in mp.keys():
                    if mp[i].val== f:
                        current.random = mp[i]
                        break
            root= root.next
            j+=1
        return mp[0]
            
            