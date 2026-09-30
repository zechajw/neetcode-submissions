# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            return 1 + max(height(root.left), height(root.right))

        # empty tree is balanced
        if root is None:
            return True 

        left_height = height(root.left)
        right_height = height(root.right)

        return abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)