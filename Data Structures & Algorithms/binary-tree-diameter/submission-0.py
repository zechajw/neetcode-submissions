# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def height(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            return 1 + max(height(root.left), height(root.right))
        
        if not root:
            return 0

        left_height = height(root.left)
        right_height = height(root.right)

        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(left_height + right_height, sub)


        return sub