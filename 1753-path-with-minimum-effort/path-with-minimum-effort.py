class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        row = len(heights)
        col = len(heights[0])

        minHeap = [[0,0,0]] # [diff,row,col]
        visited = set()

        while minHeap:
            diff,r,c = heapq.heappop(minHeap)

            if r == row-1 and c == col-1:
                return diff

            if (r,c) in visited:
                continue
            
            visited.add((r,c))

            for dr,dc in directions:
                newR, newC = r + dr, c+dc
                if(newR < 0 or newC < 0 or newR == row or newC == col or (newR, newC) in visited):
                    continue
                
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minHeap,(newDiff, newR, newC))
            


        