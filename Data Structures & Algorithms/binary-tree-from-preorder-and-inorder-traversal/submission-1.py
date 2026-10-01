# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indexes = {node: i for i, node in enumerate(inorder)}
        def helper(preorder_start: int, preorder_end: int, inorder_start: int, inorder_end: int) -> TreeNode:
            if preorder_start > preorder_end:
                return None  

            root = TreeNode(preorder[preorder_start])

            inorder_root_index = inorder_indexes[preorder[preorder_start]]

            left_inorder_start, left_inorder_end = inorder_start, inorder_root_index - 1
            left_tree_size = left_inorder_end - left_inorder_start + 1
            left_preorder_start, left_preorder_end = preorder_start + 1, preorder_start + left_tree_size

            right_inorder_start, right_inorder_end = inorder_root_index + 1, inorder_end
            right_preorder_start, right_preorder_end = left_preorder_end + 1, preorder_end

            root.left = helper(left_preorder_start, left_preorder_end, left_inorder_start, left_inorder_end)
            root.right = helper(right_preorder_start, right_preorder_end, right_inorder_start, right_inorder_end)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)