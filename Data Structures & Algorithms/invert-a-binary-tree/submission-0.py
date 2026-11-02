# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def ini(node):
            if not node:return None
            curr = TreeNode(node.val)
            curr.left = ini(node.right)
            curr.right = ini(node.left)
            return curr
        return ini(root)