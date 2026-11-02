# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxd(node,level):
            if not node:return level
            m1 = maxd(node.left,level+1)
            m2 = maxd(node.right,level+1)
            return max(m1,m2)
        return maxd(root,0)