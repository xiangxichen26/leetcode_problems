class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = [0] * (n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + nums[i]
        
        res = 0
        diff_idx = {}
        for i in range(n+1):
            need = preSum[i] - k
            if need in diff_idx:
                res = max(res, i - diff_idx[need])
            if preSum[i] not in diff_idx:  # 只记录 `preSum` 第一次出现的位置
                diff_idx[preSum[i]] = i
        
        return res
        