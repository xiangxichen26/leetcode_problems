class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._m = len(matrix)
        self._n = len(matrix[0])
        self.preSum = [[0]*(self._n+1) for _ in range(self._m)]

        for i in range(self._m):
            for j in range(1,self._n+1):
                self.preSum[i][j] = self.preSum[i][j-1] + matrix[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            ans += self.preSum[i][col2+1] - self.preSum[i][col1]
        return ans

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)