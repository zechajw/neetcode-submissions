# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root: Optional[TreeNode], min_value: int, max_value: int) -> bool:
            if not root:
                return True

            if not (min_value <= root.val <= max_value):
                return False

            return dfs(root.left, min_value, root.val - 1) and dfs(root.right, root.val + 1, max_value)

        return dfs(root, -math.inf, math.inf)
                