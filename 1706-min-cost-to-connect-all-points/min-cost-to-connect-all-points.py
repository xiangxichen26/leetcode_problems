class Solution:
    def m_distance(self, x1, x2):
        return abs(x1[0]-x2[0]) + abs(x1[1]-x2[1])
    
    def prim(self, n:int, graph:dict) -> int:
        visited = [False] * n
        hp = []
        heapq.heappush(hp,(0,0))
        ans = 0

        while hp:
            w,node = heapq.heappop(hp)

            if visited[node]:
                continue
            visited[node] = True
            ans += w

            for nei_w,nei in graph[node]:
                if not visited[nei]:
                    heapq.heappush(hp,(nei_w,nei))
        
        return ans


    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = collections.defaultdict(list)

        for i in range(n):
            for j in range(i+1,n):
                d = self.m_distance(points[i], points[j])
                graph[i].append((d, j))
                graph[j].append((d, i))
        
        return self.prim(n,graph)
        