class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        preSum = [ [0]*(n+1) for _ in range(m+1) ]
        for i in range(1,m+1):
            for j in range(1,n+1):
                preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] + mat[i-1][j-1] -preSum[i-1][j-1]
        ans = [[0]*(n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = i-k if i-k >= 0 else 0
                r2 = i+k if i+k < m else m-1
                c1 = j-k if j-k >= 0 else 0  
                c2 = j+k if j+k < n else n-1
                upper_left = [r1,c1]
                lower_right = [r2,c2]
                ans[i][j] = preSum[r2+1][c2+1] - preSum[r1][c2+1] -  preSum[r2+1][c1] + preSum[r1][c1]
        return ans
