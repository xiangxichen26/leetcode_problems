class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        pq = []
        for i in range(n):
            heapq.heappush(pq, (nums[i], i))
        
        ans = 0
        mod = 10**9 + 7

        for i in range(right):
            num, index = heapq.heappop(pq)

            if i >= left - 1:
                ans = (ans + num) % mod
            
            if index+1 < n:
                sum_pair = (num + nums[index+1], index + 1)
                heapq.heappush(pq,sum_pair)
        
        return ans


