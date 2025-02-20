class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)

        if n < 1:
            return []

        right_max = float('-inf')
        res = []
        
        for i in range(n-1,-1,-1):
            if heights[i] > right_max:
                res.append(i)
                right_max = heights[i]
        
        res.reverse()

        return res