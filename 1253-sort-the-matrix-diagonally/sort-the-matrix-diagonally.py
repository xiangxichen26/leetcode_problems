class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diagonals = {}

        for i in range(m):
            for j in range(n):
                diagonal = i - j
                if diagonal not in diagonals:
                    diagonals[diagonal] = []
                diagonals[diagonal].append(mat[i][j])
        
        for diagonal in diagonals.values():
            diagonal.sort(reverse=True)
        
        for i in range(m):
            for j in range(n):
                diagonal = i - j
                mat[i][j] = diagonals[diagonal].pop()
        
        return mat



        