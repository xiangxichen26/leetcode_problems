class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in val_to_index:
                return [val_to_index[need], i]
            
            val_to_index[nums[i]] = i
        
        return []
