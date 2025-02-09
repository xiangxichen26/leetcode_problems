class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSumToIndex = {}
        res = 0

        preSum = 0
        preSumToIndex[0] = -1

        for i,num in enumerate(nums):
            preSum += num
            need = preSum - k
            if need in preSumToIndex:
                res = max(res, i - preSumToIndex[need])  # 更新最长子数组长度
            if preSum not in preSumToIndex:  # 只记录 `preSum` 第一次出现的位置
                preSumToIndex[preSum] = i
        
        return res
        