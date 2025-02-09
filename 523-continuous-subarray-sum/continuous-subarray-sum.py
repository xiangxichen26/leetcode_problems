class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preSum = 0
        preSum_to_index = {}
        
        preSum_to_index[0] = -1
        zero_count = 0

        for i, num in enumerate(nums):
            preSum += num
            need = preSum % k

            if need in preSum_to_index:
                length = i - preSum_to_index[need]
                if length >= 2:
                    return True
            
            if preSum % k not in preSum_to_index:
                preSum_to_index[preSum % k] = i
        
        return False