class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
            # initialize a minDist array
            minDist = [float('inf')] * n
            minDist[src] = 0

            # relaxtion k times
            for _ in range(k+1):
                temp = minDist.copy()
                for u,v,w in flights:
                    if minDist[u] != float('inf') and minDist[u]+w < temp[v]:
                        temp[v] = minDist[u]+w
                minDist = temp

            if minDist[dst] == float('inf'):
                return -1
            return minDist[dst]
