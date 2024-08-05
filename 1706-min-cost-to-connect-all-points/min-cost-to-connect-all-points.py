class UnionFind:
    def __init__(self, n:int):
        self.parent = [i for i in range(n)]
        self.count = n
    
    def find(self,x):
        if self.parent[x] != x:
		        # generation compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        
        self.parent[root_x] = root_y
        self.count -= 1
    
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def m_distance(self, x1, x2):
        return abs(x1[0]-x2[0]) + abs(x1[1]-x2[1])
    
    def kruskal(self, n:int, edges: list) -> int:
        union_find = UnionFind(n)

        edges.sort(key=lambda x:x[2])
        ans = 0
        count = 0

        for u,v,w in edges:
            if union_find.is_connected(u, v):
                continue
            
            ans += w
            count += 1
            union_find.union(u, v)
            
            if count == n-1:
                return ans
        
        return ans

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i+1,n):
                d = self.m_distance(points[i], points[j])
                edges.append([i,j,d])
        
        return self.kruskal(n,edges)
        