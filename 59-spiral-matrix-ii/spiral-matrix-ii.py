class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        upper_bound, lower_bound = 0, n - 1
        left_bound, right_bound = 0, n - 1
        res = [[0]*n for _ in range(n)]
        print(res)
        count = 0

        while count < n*n:
            if upper_bound <= lower_bound:
                for j in range(left_bound, right_bound + 1):
                    count += 1
                    res[upper_bound][j] = count
                upper_bound += 1
            
            if left_bound <= right_bound:
                for i in range(upper_bound, lower_bound + 1):
                    count += 1
                    res[i][right_bound] = count
                right_bound -= 1

            if upper_bound <= lower_bound:
                for j in range(right_bound, left_bound - 1, -1):
                    count += 1
                    res[lower_bound][j] = count
                lower_bound -= 1
            
            if left_bound <= right_bound:
                for i in range(lower_bound, upper_bound - 1, -1):
                    count += 1
                    res[i][left_bound] = count
                left_bound += 1
        
        return res




        