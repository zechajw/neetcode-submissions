# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node: TreeNode, max_so_far: int) -> int:
            if not node:
                return 0

            new_max = max(max_so_far, node.val)

            good_nodes = helper(node.left, new_max) + helper(node.right, new_max)

            if node.val >= max_so_far:
                good_nodes += 1

            return good_nodes

        if not root:
            return 0

        return helper(root, root.val)