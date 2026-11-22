# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        current = TreeNode(preorder[0])
        mid = -1
        for i in range(len(inorder)):
            if inorder[i]==preorder[0]:
                mid = i
                break
        if mid ==-1:
            return current
        lefthalf = inorder[:mid]
        righthalf = inorder[mid+1:]
        current.left = self.buildTree(preorder[1:mid+1],lefthalf)
        current.right = self.buildTree(preorder[mid+1:],righthalf)
        return current