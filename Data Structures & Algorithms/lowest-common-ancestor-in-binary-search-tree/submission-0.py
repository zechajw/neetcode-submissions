# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Case 1: root is p or root is q, then return root
        # Case 2: root is None, then return None
        # Case 3: lca(root.left) == p/q and lca(root.right) == p/q, then return root
        # Case 4: lca(root.left) == p/q and lca(root.right) == None then return root.left
        # Case 5: lca(root.right) == p/q and lca(root.left) == None then return root.right

        if root is None:
            return None

        if root == p or root == q:
            return root

        lca_left = self.lowestCommonAncestor(root.left, p, q)
        lca_right = self.lowestCommonAncestor(root.right, p, q)

        if lca_left and lca_right:
            return root
        elif lca_left and not lca_right:
            return lca_left
        else:
            return lca_right

        