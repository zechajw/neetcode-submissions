class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [node for node in range(n)]
        rank = [0 for node in range(n)]

        def find(node: int) -> int:
            while parents[node] != node:
                parents[node] = parents[parents[node]]
                node = parents[node]

            return parents[node]

        def union(node1: int, node2: int) -> False:
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return False

            rank1, rank2 = rank[parent1], rank[parent2]

            if rank1 == rank2:
                parents[parent2] = parent1
                rank[parent1] += 1
            elif rank1 > rank2:
                parents[parent2] = parent1
            else:
                parents[parent1] = parent2

            return True

        components = n
        for node1, node2 in edges:
            if union(node1, node2): # nodes were not in same component
                components -= 1
        
        return components