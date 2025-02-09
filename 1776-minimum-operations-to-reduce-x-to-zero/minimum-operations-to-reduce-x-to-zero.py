class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        new_x = sum(nums) - x
        if new_x ==0 :
            return len(nums)
        
        length = 0
        preSum = 0
        preSum_to_index = {0:-1}
        
        for i,num in enumerate(nums):
            preSum += num
            need = preSum - new_x

            if need in preSum_to_index:
                length = max(length,i - preSum_to_index[need])

            if preSum not in preSum_to_index:
                preSum_to_index[preSum] = i
        return len(nums) - length if length else -1

        