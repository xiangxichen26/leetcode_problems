class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        res = [[0]*n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                origin_index = row * n + col
                new_index = (origin_index + k) % (m*n)
                i = new_index // n
                j = new_index % n
                res[i][j] = grid[row][col]
        return res

                
        
