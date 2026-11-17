# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = []
        def travel(node,maxTillNow):
            if not node:
                return
            if node.val>=maxTillNow:
                # print(node.val)
                ans.append(1)
            travel(node.right,max(maxTillNow,node.val))
            travel(node.left,max(maxTillNow,node.val))
            return 
        travel(root,-float('inf'))
        return sum(ans)
            