class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = 0
        count = 0
        preSum_to_count = {}
        preSum_to_count[0] = 1
        for i, num in enumerate(nums):
            preSum += num
            need = preSum - k
            if need in preSum_to_count:
                count += preSum_to_count[need]
            if preSum not in preSum_to_count:
                preSum_to_count[preSum] = 1
            else:
                preSum_to_count[preSum] = preSum_to_count[preSum] + 1
        
        return count