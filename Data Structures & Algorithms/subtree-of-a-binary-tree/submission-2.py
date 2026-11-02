class Solution:

  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot:
      return True
    if not root:
      return False

    # 1. If the trees are completely identical starting from here, return True
    if self.sameTree(root, subRoot):
      return True

    # 2. Otherwise, keep subRoot anchored and search deeper in root.left or root.right
    return self.isSubtree(root.left, subRoot) or self.isSubtree(
        root.right, subRoot
    )

  def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Strict comparison: checks if two trees are exact clones of each other
    if not p and not q:
      return True
    if not p or not q or p.val != q.val:
      return False

    return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)