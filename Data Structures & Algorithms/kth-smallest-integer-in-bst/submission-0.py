# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []

        def traverse(root: Optional[TreeNode]) -> None:
            if len(in_order) >= k:
                return

            if root is None:
                return

            traverse(root.left)
            in_order.append(root.val)
            traverse(root.right)

        traverse(root)

        return in_order[k - 1]