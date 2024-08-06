class UnionFind:
    def __init__(self,n:int):
        self.parent = [i for i in range(n)]
        self.count = n
    
    def find(self,x):
        if x!= self.parent[x]:
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
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row_size = len(heights)
        col_size = len(heights[0])
        size = row_size * col_size
        edges = []

        for row in range(row_size):
            for col in range(col_size):
                if row < row_size - 1:
                    x = row * col_size + col
                    y = (row + 1) * col_size + col
                    h = abs(heights[row][col] - heights[row + 1][col])
                    edges.append([x, y, h])
                if col < col_size - 1:
                    x = row * col_size + col
                    y = row * col_size + col + 1
                    h = abs(heights[row][col] - heights[row][col + 1])
                    edges.append([x, y, h])
        
        edges.sort(key=lambda x: x[2])
        union_find = UnionFind(size)

        for x, y, h in edges:
            union_find.union(x, y)
            if union_find.is_connected(0, size - 1):
                return h
        return 0

       