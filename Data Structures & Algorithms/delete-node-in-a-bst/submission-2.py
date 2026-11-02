# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dele(parent,current):
            if not current:
                return None
            if current.val == key:
                if not current.left :
                    return current.right
                elif not current.right:
                    return current.left
                else:
                    new_child = current.right
                    new_end = new_child.left
                    if not new_end:
                        new_child.left = current.left
                    else:
                        while new_end and new_end.left:
                            new_end = new_end.left
                        new_end.left = current.left
                    return new_child
            if current.val>key:
                current.left = dele(current,current.left)
            else:
                current.right =dele(current,current.right)
            return current
        return dele(None,root)