# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans = 0 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def travel(node):
            if not node : return 0
            left = travel(node.left)+1
            right = travel(node.right)+1
            self.ans =max(self.ans,left+right-2)
            return max(left,right)
        travel(root)
        return self.ans

