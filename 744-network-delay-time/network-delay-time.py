class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Bellman Ford

        #initialize a minDict array
        minDist = [float('inf')] * n
        minDist[k-1] = 0

        # relax all the edges n-1 times
        for _ in range(n-1):
            for u,v,w in times:
                if minDist[u-1] != float('inf') and minDist[u-1]+w < minDist[v-1]:
                    minDist[v-1] = minDist[u-1]+w
        
        ans = -1
        for i in minDist:
            if i == float('inf'):
                return -1
            if i > ans:
                ans = i
        return ans