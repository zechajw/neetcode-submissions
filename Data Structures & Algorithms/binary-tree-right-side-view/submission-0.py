# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side = []

        if not root:
            return right_side

        curr_level = [root]

        while curr_level:
            right_side.append(curr_level[-1].val)

            next_level = []

            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            curr_level = next_level

        return right_side       