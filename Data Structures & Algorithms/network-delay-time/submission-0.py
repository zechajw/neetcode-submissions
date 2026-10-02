import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [math.inf for node in range(n + 1)]

        distances[k] = 0

        adj_list = defaultdict(list)

        for source, dest, time in times:
            adj_list[source].append([dest, time])

        dijkstras = []

        heapq.heappush(dijkstras, (k, 0))

        while dijkstras:
            node, distance = heapq.heappop(dijkstras)

            # skip stale entries
            if distances[node] < distance:
                continue

            for neighbour, time in adj_list[node]:
                if distances[neighbour] > distances[node] + time:
                    distances[neighbour] = distances[node] + time
                    heapq.heappush(dijkstras, [neighbour, distances[neighbour]])

        time_taken = max(distances[1:])

        return -1 if time_taken == math.inf else time_taken
                