class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # build a graph
        graph = dict()
        for i in range(n):
            graph[i] = 0

        # calcuate the edges
        for u,v in roads:
            graph[u] = graph.get(u) + 1
            graph[v] = graph.get(v) + 1

        hp = []
        for i in range(n):
            heapq.heappush(hp,(graph[i],i))
        
        ans = 0
        for i in range(n):
            n,node = heapq.heappop(hp)
            ans = ans + graph[node] * (i+1)
        
        return ans




