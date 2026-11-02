# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    mx=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       
        def loop(node):
            if not node:
                return 0
            l = loop(node.left)
            r = loop(node.right)
            self.mx= max(self.mx,l+r)
            return 1+ max(l,r)
        loop(root)
        return self.mx
            