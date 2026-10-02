"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def dfs(node: Optional['Node']):
            if not node:
                return

            clones[node] = Node(node.val)

            for neighbour in node.neighbors:
                if neighbour not in clones:
                    dfs(neighbour)

        dfs(node)
        for original, clone in clones.items():
            clone.neighbors = [clones[neighbour] for neighbour in original.neighbors]

        return clones[node] if node else None