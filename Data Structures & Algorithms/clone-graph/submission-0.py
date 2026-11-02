"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}
        if not node:return None
        explore = [node]
        while explore:
            n = explore.pop()
            if nodes.get(n.val,-1)==-1:
                nodes[n.val] = Node(n.val)
                for i in n.neighbors:
                    explore.append(i)
        explore = [node]
        complete = set()
        while explore:
            n = explore.pop()
            if n.val not in complete:
                l = []
                for i in n.neighbors:
                    l.append(nodes[i.val])
                    explore.append(i)
                nodes[n.val].neighbors = l
                complete.add(n.val)

        return nodes[1]