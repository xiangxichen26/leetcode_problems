class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build the graph
        graph = collections.defaultdict(list)
        for (u, v, w) in times:
            graph[u].append((v, w))

        # initialize the shortest path
        shortest_dict = {}

        # initialize the min heap
        pq = []
        heapq.heappush(pq,(0,k))

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            if current_node in shortest_dict:
                continue
            
            shortest_dict[current_node] = current_dist

            # Relaxation
            for nei_node, nei_weight in graph[current_node]:
                if nei_node in shortest_dict:
                    continue
                heapq.heappush(pq,(current_dist + nei_weight, nei_node))

        if len(shortest_dict) == n:
            return max(shortest_dict.values())
        else:
            return -1
