class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        preSum = [0] * (n+1)
        preSum[0] = 0
        for i in range(1,n+1):
            preSum[i] = preSum[i-1] + nums[i-1]
        
        for i in range(n):
            left_sum = preSum[i]
            right_sum = preSum[n] - preSum[i+1]
            if left_sum == right_sum:
                return i
        return -1






        