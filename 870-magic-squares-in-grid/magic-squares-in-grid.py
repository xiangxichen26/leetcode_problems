class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # edge case
        rows = len(grid)
        cols = len(grid[0])
        
        if rows < 3 or cols < 3:
            return 0

        def helper(r,c) -> int:
            # Ensure 1-9
            values = set()
            for i in range(r,r+3):
                for j in range(c, c+3):
                    if (grid[i][j] in values) or not (1 <= grid[i][j] <= 9):
                        return 0
                    values.add(grid[i][j])
            
            # Calcuate the Rows
            for i in range(r, r+3):
                if sum(grid[i][c:c+3]) != 15:
                    return 0 

            # Calcuate the Cols
            for j in range(c, c+3):
                if grid[r][j]+grid[r+1][j]+grid[r+2][j] != 15:
                    return 0

            # Calcuate the Diagonals
            if (
                grid[r][c] + grid[r+1][c+1]+ grid[r+2][c+2] != 15 or 
                grid[r][c+2] + grid[r+1][c+1]+ grid[r+2][c] != 15):
                return 0
            
            return 1

        ans = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                ans = ans + helper(i,j)
        
        return ans




