class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        res_grid = [[0]*n for _ in range(m)]

        while k:
            res_grid = [[0]*n for _ in range(m)]
            # Step 1 Element at grid[i][j] moves to grid[i][j + 1].
            for i in range(m):
                res_grid[i][1:n]= grid[i][0:n-1]

            # Step 2 Element at grid[i][n - 1] moves to grid[i + 1][0].
            for i in range(m-1):
                res_grid[i+1][0] = grid[i][n - 1]

            # step 3
            res_grid[0][0] = grid[m - 1][n - 1]
            
            k -= 1
            grid = res_grid
        
        return grid
        
