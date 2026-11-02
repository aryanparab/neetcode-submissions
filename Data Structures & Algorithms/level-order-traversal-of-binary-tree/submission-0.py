# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def add_level(level,root):
            if not root:return
            if level not in levels:
                levels[level]=[]
            levels[level].append(root.val)
            add_level(level+1,root.left)
            add_level(level+1,root.right)
        levels = {}
        i =0

        add_level(i,root)
        return list(levels.values())