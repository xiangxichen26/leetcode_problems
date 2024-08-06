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

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Directions: down, up, right, left

        for row in range(row_size):
            for col in range(col_size):
                current = row * col_size + col
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < row_size and 0 <= new_col < col_size:
                        neighbor = new_row * col_size + new_col
                        diff = abs(heights[row][col] - heights[new_row][new_col])
                        edges.append([current, neighbor, diff])
        
        edges.sort(key=lambda x: x[2])
        union_find = UnionFind(size)

        for x, y, h in edges:
            union_find.union(x, y)
            if union_find.is_connected(0, size - 1):
                return h
        return 0

       