class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #SPFA
        # create a graph
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append([v,w])
        
        #initialize a minDict array
        minDist = [float('inf')] * (n+1)
        minDist[k] = 0

        queue = deque()
        queue.append(k)

        # relax all the edges n-1 times
        while queue:
            node = queue.popleft()
            for nei,nei_w in graph[node]:
                if minDist[node]!= float('inf') and minDist[node] + nei_w < minDist[nei]:
                     minDist[nei] = minDist[node] + nei_w
                     if nei not in queue:
                        queue.append(nei)
        
        ans = -1
        for i in range(1,n+1):
            if minDist[i] == float('inf'):
                return -1
            if minDist[i] > ans:
                ans = minDist[i]
        return ans