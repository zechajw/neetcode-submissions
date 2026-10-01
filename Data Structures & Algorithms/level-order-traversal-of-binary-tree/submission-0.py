# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # initialize result array
        result = []

        if not root:
            return result

        # add (root, 0) to bfs queue
        bfs = deque()
        bfs.appendleft((root, 0))


        # while bfs is not empty:
        while bfs:
            node, level = bfs.pop()

            if len(result) == level:
                result.append([])

            result[level].append(node.val)

            if node.left:
                bfs.appendleft((node.left, level + 1))
            
            if node.right:
                bfs.appendleft((node.right, level + 1))

        return result


        # Trace Input: root = [1,2,3,4,5,6,7]

        # result = [[1], [2]]
        # bfs = [(2_node, 1), (3_node, 1)]

        # pop (root, 0)
            # len(result) == level, so append [] to result
            # level = 0, so append root.val to the level at index 0
            # append root.left, 1 to bfs
            # append root.right, 1 to bfs 
        # pop (2_node, 1)
            # len(result) == level, so append [] to result 
            # level = 1, so append 2_node.val to the level at index 1
            # append 4_node, 2 to bfs
            # append 5_node, 2 to bfs
        # ...
        

                