class Solution:
    def rotate(self, matrix):
        # 将二维矩阵原地顺时针旋转 90 度
        n = len(matrix)
        # 先沿对角线镜像对称二维矩阵
        for i in range(n):
            for j in range(i, n):
                # swap(matrix[i][j], matrix[j][i]);
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 然后反转二维矩阵的每一行
        for row in matrix:
            row.reverse()
        